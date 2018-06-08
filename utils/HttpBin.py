import requests


class HttpBin(object):
    """Class for work with api"""

    def request_method_get(self, url, header):
        """ Method for get request
        Args:
            url: url for get request
            header: dictionary with user's header
        Returns:
            response: response after get request
        """
        response = requests.get(url, headers=header)
        return response

    def response_method_get_headers(self, response):
        """ Method for get headers from response
        Args:
            response: response after get request
        Returns:
            headers: headers after get request with user's header
        """
        headers = response.json()["headers"]
        return headers

    def request_method_stream(self, url):
        """Method for stream request
        Keyword Args:
            url: url for stream request
        Returns:
            response: response after stream request
        """
        response = requests.get(url)
        return response

    def response_methos_get_count_rows(self, response):
        """Method for stream request
        Keyword Args:
            response: response after stream request
        Returns:
            count_rows_from_response: count json rows from response
        """
        count_rows_from_response = len(response.content.split('\n')) - 1
        return count_rows_from_response

    def request_basic_auth(self, url, login, password):
        """Method for basic auth
        Keyword Args:
            url: url for basic auth
            login: login for basic auth
            password: password for basic auth
        Returns:
            response: response after basic auth request
        """
        response = requests.get(url, auth=(login, password))
        return response

    def response_get_status_code(self, response):
        """Method for get status code
        Keyword Args:
            response: response after any request
        Returns:
            status_code: status code from response
        """
        status_code = response.status_code
        return status_code

    def request_post_request_with_query_string(self, url):
        """Method for post request with query string
        Keyword Args:
            url: url for post request with query string
        Returns:
            response: response after post request with query string
        """
        response = requests.post(url=url)
        return response

    def response_method_get_args(self, response):
        """ Method for get args from response
        Args:
            response: response after post request with query string
        Returns:
            args: args after post request with query string
        """
        args = response.json()["args"]
        return args

    def request_post_with_body(self, url, body):
        """ Method for post request with body
        Args:
            url: url for post request with body
            body: body for post request
        Returns:
            response: response after post request with body
        """
        response = requests.post(url=url, data=body)
        return response

    def response_method_get_data(self, response):
        """ Method for get data from response
        Args:
            response: response after post request with body
        Returns:
            data: data after post request with body
        """
        data = response.json()["data"]
        return data
