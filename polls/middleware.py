import time

from polls.models import Result


class ResultMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        end_time = time.time()
        execution_time = end_time - start_time
        print("gfg")
        with open('result.txt', 'a') as f:
            f.write(f"Path: {request.path}, Method: {request.method}, Time: {execution_time}\n")

        result = Result(path=request.path, method=request.method, execution_time=execution_time)
        result.save()

        return response
