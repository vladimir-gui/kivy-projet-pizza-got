import json
from kivy.network.urlrequest import UrlRequest


class HttpClient:
    def get_pizzas(self, on_complete_received_data, on_error):
        url = "https://got-pizzamamadjango.herokuapp.com/api/GetPizza"

        def data_received(request, result):
            # for key, value in result['headers'].items():
            #     print('{}: {}'.format(key, value))
            data = json.loads(result)
            pizza_dictionnaire = []
            for pizza in data:
                pizza_dictionnaire.append(pizza["fields"])

            if on_complete_received_data:
                on_complete_received_data(pizza_dictionnaire)

        def data_error(request, error_message):
            print("data error" + str(error_message))

        def data_failure(request, failure_message):
            # print("data failure" + str(failure_message))
            if on_error:
                on_error("Erreur serveur :" + str(request.resp_status))

        request = UrlRequest(url, on_success=data_received, on_error=data_error, on_failure=data_failure)
