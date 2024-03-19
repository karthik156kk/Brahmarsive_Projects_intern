from karthik_blog_website import app
from karthik_blog_website.models import Post
from testing.conftest import setup_test_user_for_login, setup_test_post_from_test_user
from flask_login import current_user


def test_create_post(client):
    with app.app_context():
        setup_test_user_for_login(client, 'test@example.com', 'password123')
        response = client.get('/post/new')
        assert response.status_code == 200
        response = client.post('/post/new', data={
            'title': 'Test Post',
            'content': 'This is a test post content'
        }, follow_redirects=True)
        assert response.status_code == 200
        post = Post.query.filter_by(title='Test Post').first()
        assert post is not None


def test_update_post(client):
    with app.app_context():
        setup_test_user_for_login(client, 'test@example.com', 'password123')
        post = setup_test_post_from_test_user()
        response = client.post(f'/post/{post.id}/update', data={
            'title': 'Updated Test Post',
            'content': 'This is the updated test post content'
        }, follow_redirects=True)
        assert response.status_code == 200
        assert b'Your post has been updated!' in response.data
        updated_post = Post.query.filter_by(id=post.id).first()
        assert updated_post is not None
        assert updated_post.title == 'Updated Test Post'
        assert updated_post.content == 'This is the updated test post content'
        assert updated_post.user_id == current_user.id


def test_delete_post(client):
    with app.app_context():
        setup_test_user_for_login(client, 'test@example.com', 'password123')
        post = setup_test_post_from_test_user()
        response = client.post(f'/post/{post.id}/delete', follow_redirects=True)
        assert response.status_code == 200
        assert b'Your post has been Deleted!' in response.data
        deleted_post = Post.query.filter_by(id=post.id).first()
        assert deleted_post is None