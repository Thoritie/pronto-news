from django.test import TestCase
from django.urls import reverse

from ..models import Post
class PostListViewTest(TestCase):
    def test_post_list_view_should_be_accessible(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_list_view_should_show_list_of_posts(self):
        Post.objects.create(
            title='Hello World',
            url='http://hello.world.me'
        )
        Post.objects.create(
            title='Hello Woof',
            url='http://hello.woof.me'
        )

        response = self.client.get(reverse('post_list'))
        expected = '<li><a href="http://hello.world.me" ' \
            'target="_blank">Hello World</a></li>' \
            '<li><a href="http://hello.woof.me" ' \
            'target="_blank">Hello Woof</a></li>' \

        self.assertContains(response, expected, status_code = 200)
