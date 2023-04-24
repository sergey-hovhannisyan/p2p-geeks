from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from django.db.models import Count
from .models import Profile, Skill, Interest
from django.db.models import Value, FloatField

def match_users(profile):
    # Retrieve the user's profile
    user_profile = Profile.objects.get(user=profile.user)

    # Calculate the similarity scores based on skills
    user_skills = Skill.objects.filter(user=profile.user).values_list('skill', flat=True)
    user_interests = Interest.objects.filter(user=profile.user).values_list('interest', flat=True)
    all_profiles = Profile.objects.exclude(user=profile.user).exclude(user__is_superuser=True)
    profiles_skills = all_profiles.annotate(num_skills=Count('user__skill')).filter(num_skills__gt=0).values_list('user__skill__skill', flat=True)
    profile_interests = all_profiles.annotate(num_interests=Count('user__interest')).filter(num_interests__gt=0).values_list('user__interest__interest', flat=True)
    vectorizer = CountVectorizer()
    skills_matrix = vectorizer.fit_transform([', '.join(user_skills), ', '.join(profiles_skills)])
    skills_similarity = cosine_similarity(skills_matrix)[0, 1]
    interest_matrix = vectorizer.fit_transform([', '.join(user_interests), ', '.join(profile_interests)])
    interest_similarity = cosine_similarity(interest_matrix)[0, 1]

    # Calculate the similarity scores based on school name
    school_similarity = 1 if user_profile.school_name == all_profiles.exclude(school_name__exact='').values_list('school_name', flat=True).distinct().first() else 0

    # Calculate the overall similarity scores
    overall_similarity = skills_similarity + interest_similarity + school_similarity

    # Rank the matches
    matched_profiles = all_profiles.annotate(similarity=Value(overall_similarity, output_field=FloatField())).order_by('-similarity')

    return matched_profiles
