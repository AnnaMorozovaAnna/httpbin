from utils.HttpBin import HttpBin
import pytest


@pytest.mark.parametrize("url, header", [
    ('https://httpbin.org/get', {'Headeranna': 'test_value'})
])
def test_get_check_header(url, header):
    """Test for get request for header and check user's header"""
    http_bin = HttpBin()
    response = http_bin.request_method_get(url, header)
    result_header_from_response = http_bin.response_method_get_headers(response)
    expected_header = header.keys()[0]
    expected_value = header.values()[0]
    actual_value = result_header_from_response.get(expected_header)
    status_code = 200
    actual_status_code = http_bin.response_get_status_code(response)
    assert status_code == actual_status_code
    assert expected_value == actual_value


@pytest.mark.parametrize("url, count_rows", [
    ('http://httpbin.org/stream/', 20),
    ('http://httpbin.org/stream/', 120)  # this is a bug, service can not return more than 100 rows
])
def test_stream_check_count_rows(url, count_rows):
    """Test for get request for stream and check count rows of stream response"""
    http_bin = HttpBin()
    response = http_bin.request_method_stream(url + str(count_rows))
    actual_result = http_bin.response_methos_get_count_rows(response)
    status_code = 200
    actual_status_code = http_bin.response_get_status_code(response)
    assert status_code == actual_status_code
    assert actual_result == count_rows


@pytest.mark.parametrize("url, status_code, login, password", [
    ('http://httpbin.org/basic-auth/user/passwd', 200, "user", "passwd"),
    ('http://httpbin.org/basic-auth/user/passwd', 401, "user", "parsswd")
])
def test_basic_auth(url, status_code, login, password):
    """Test for basic authentication"""
    http_bin = HttpBin()
    response = http_bin.request_basic_auth(url, login, password)
    actual_status_code = http_bin.response_get_status_code(response)
    assert status_code == actual_status_code


@pytest.mark.parametrize("url, status_code, parameter, value", [
    ('http://httpbin.org/post', 200, "user", "passwd"),
])
def test_post_query_string(url, status_code, parameter, value):
    """Test for check post response after post request with query string"""
    http_bin = HttpBin()
    query_string = "?%s=%s" % (parameter, value)
    actual_url = url + query_string
    response = http_bin.request_post_request_with_query_string(actual_url)
    args = http_bin.response_method_get_args(response)
    actual_parameter = args.keys()[0]
    actual_value = args.values()[0]
    assert actual_parameter == parameter
    assert actual_value == value
    actual_status_code = http_bin.response_get_status_code(response)
    assert status_code == actual_status_code


@pytest.mark.parametrize("url, status_code, body", [
    ('http://httpbin.org/post', 200, "text for body test"),
])
def test_post_with_body(url, status_code, body):
    """Test for check post response after post request with body"""
    http_bin = HttpBin()
    response = http_bin.request_post_with_body(url, body)
    actual_body_from_data = http_bin.response_method_get_data(response)
    assert actual_body_from_data == body
    actual_status_code = http_bin.response_get_status_code(response)
    assert status_code == actual_status_code
