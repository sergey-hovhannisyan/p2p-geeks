from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from django.db.models import Count
from .models import Skill, Profile, Follow

def match_users(profile):
    # Retrieve the user's profile
    user_profile = Profile.objects.get(user=profile.user)

    # Calculate the similarity scores based on skills
    user_skills = Skill.objects.filter(user=profile.user).values_list('skill', flat=True)
    all_profiles = Profile.objects.exclude(user=profile.user)
    profiles_skills = all_profiles.annotate(num_skills=Count('user__skill')).filter(num_skills__gt=0).values_list('user__skill__skill', flat=True)
    vectorizer = CountVectorizer()
    skills_matrix = vectorizer.fit_transform([', '.join(user_skills), ', '.join(profiles_skills)])
    skills_similarity = cosine_similarity(skills_matrix[0], skills_matrix[1])

    # Calculate the similarity scores based on GPA
    gpa_similarity = 1 - abs(user_profile.gpa - all_profiles.exclude(gpa__isnull=True).values_list('gpa', flat=True)) / 4

    # Calculate the similarity scores based on school name
    school_similarity = 1 if user_profile.school_name == all_profiles.exclude(school_name__exact='').values_list('school_name', flat=True).distinct() else 0

    # Calculate the similarity scores based on followers
    followers_similarity = Follow.objects.filter(following=profile.user).values_list('follower', flat=True)
    followers_similarity = len(set(followers_similarity) & set(all_profiles.values_list('user__username', flat=True))) / len(all_profiles)

    # Calculate the overall similarity scores
    overall_similarity = skills_similarity + gpa_similarity + school_similarity + followers_similarity

    # Rank the matches
    matched_profiles = all_profiles.annotate(similarity=overall_similarity).order_by('-similarity')
    return matched_profiles