from kivy.network.urlrequest import UrlRequest

class HttpClient:
    def get_pizza(self):
        url = "https://got-pizzamamadjango.herokuapp.com/api/GetPizza"

        def data_received(request, result):
            # for key, value in result['headers'].items():
            #     print('{}: {}'.format(key, value))
            print("data_received()")

        requests = UrlRequest(url, on_success=data_received)