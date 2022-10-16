from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post

# Create your tests here.
class TestView(TestCase):

    def setUp(self):
        self.client = Client()


    def test_post_list(self):
        # self.assertEqual(3, 3) # 괄호 안에 있는 애가 같으면 true => 지금 넣은 건 false
        response = self.client.get('/blog/')
        # 301 오류 나면 , follow=True 추가
        # response 결과가 정상적으로 보이는지
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.content, 'html.parser')

        # title이 정상적으로 보이는지
        self.assertEqual(soup.title.text, 'Blog')

        # navbar가 정상적으로 보이는지
        navbar = soup.nav
        self.assertIn('Blog', navbar.text)
        self.assertIn('About me', navbar.text)

        # port가 정상적으로 보이는지
        # 1. 맨 처음엔 post가 없음
        self.assertEqual(Post.objects.count(), 0)
        main_area = soup.find('div', id="main-area")
        self.assertIn('아직 게시물이 없습니다', main_area.text)

        # 2. post가 추가
        post_001 = Post.objects.create(title="첫 번째 포스트", content="첫 번째 포스트입니다.")
        post_002 = Post.objects.create(title="두 번째 포스트", content="두 번째 포스트입니다.")
        self.assertEqual(Post.objects.count(), 2)

        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        main_area = soup.find('div', id="main-area")
        self.assertIn(post_001.title, main_area.text)
        self.assertIn(post_002.title, main_area.text)
        self.assertNotIn('아직 게시물이 없습니다', main_area.text)