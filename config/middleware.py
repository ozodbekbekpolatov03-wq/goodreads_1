class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response=get_response

    def __call__(self, request):
        print(f"BEFORE REQUREST FOR { request.path}")
        response=self.get_response(request)
        print("AFTER GETTIBG RESPONSE")
        return response
# bu brovzer bilan viwe o'rtasidagi medil wear borligini blishi uchun