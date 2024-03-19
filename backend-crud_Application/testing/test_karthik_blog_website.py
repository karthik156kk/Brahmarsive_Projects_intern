import pytest
from karthik_blog_website import app
from testing.conftest import GENERAL_PAGE_VALIDATION_PARAMETERS, SPECIAL_PAGE_VALIDATION_PARAMETERS
from testing.conftest import SPL_PAGE_AFTER_LOGIN_VALIDATION_PARAMETERS, setup_test_user_for_login


@pytest.mark.parametrize('general_endpoint', GENERAL_PAGE_VALIDATION_PARAMETERS)
def test_general_page(client, general_endpoint):
    response = client.get(general_endpoint)
    assert response.status_code == 200


@pytest.mark.parametrize('special_endpoint', SPECIAL_PAGE_VALIDATION_PARAMETERS)
def test_special_page(client, special_endpoint):
    response = client.get(special_endpoint)
    assert response.status_code == 302 #requires the user to be logged in to access the endpoint
    print(dict(response))


@pytest.mark.parametrize('logged_spl_endpoints, output_status', SPL_PAGE_AFTER_LOGIN_VALIDATION_PARAMETERS)
def test_special_page(client, logged_spl_endpoints, output_status):
    with app.app_context():
        setup_test_user_for_login(client, 'test@example.com', 'password123')
        response = client.get(logged_spl_endpoints)
        assert response.status_code == output_status
