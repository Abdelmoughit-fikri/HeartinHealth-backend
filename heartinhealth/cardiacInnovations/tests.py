# from django.test import TestCase
# from django.contrib.auth import get_user_model
# from rest_framework.test import APITestCase
# from rest_framework import status
# from django.urls import reverse
# from .models import CdArticle

# class CardiacDiseasesViewSetTest(APITestCase):

#     @classmethod
#     def setUpTestData(cls):
#         """Set up test data for all tests"""
#         cls.user = get_user_model().objects.create_user(username="testuser", password="testpass")
#         cls.article1 = CdArticle.objects.create(
#         title="Article 1", category="Heart", sub_category="Atherosclerosis", 
#         is_important=True, author=cls.user
#     )
#         cls.article2 = CdArticle.objects.create(
#         title="Article 2", category="Heart", sub_category="Hypertension", 
#         is_important=True, author=cls.user
#     )
#         cls.article3 = CdArticle.objects.create(
#         title="Article 3", category="Cardio", sub_category="Arrhythmia", 
#         is_important=False, author=cls.user
#     )


#     def test_get_all_articles(self):
#         """Test retrieving all articles"""
#         url = reverse('cardiac-diseases-articles-list')  # Ensure correct route name
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data["articles"]), 3)  # Check total articles count
        
#     def test_filter_by_category(self):
#         """Test filtering articles by category"""
#         url = reverse('cardiac-diseases-articles-list') + "?category=Heart"
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data["articles"]), 2)  # Only "Heart" category articles

#     def test_filter_by_sub_category(self):
#         """Test filtering articles by sub-category"""
#         url = reverse('cardiac-diseases-articles-list') + "?sub_category=Atherosclerosis"
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data["articles"]), 1)

#     def test_sort_by_latest(self):
#         """Test sorting by latest"""
#         url = reverse('cardiac-diseases-articles-list') + "?latest=true"
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_sort_by_oldest(self):
#         """Test sorting by oldest"""
#         url = reverse('cardiac-diseases-articles-list') + "?oldest=true"
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_sort_by_importance(self):
#         """Test sorting by importance"""
#         url = reverse('cardiac-diseases-articles-list') + "?importance=true"
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_pagination(self):
#         """Test pagination response"""
#         url = reverse('cardiac-diseases-articles-list') + "?page=1"
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn("articles", response.data)  # Ensure paginated response


# print("Total Articles in DB:", CdArticle.objects.count())