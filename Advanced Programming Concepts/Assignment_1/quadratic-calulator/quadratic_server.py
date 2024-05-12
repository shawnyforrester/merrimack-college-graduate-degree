# Name: Shawn Forrester
# Python 3.10.6
# server.py

# imports
import grpc
import quadratic_pb2
import quadratic_pb2_grpc
from concurrent import futures

#Server class to implement each gRPC service.

class QuadraticCalculator(quadratic_pb2_grpc.CalculateServicer):
    def Calculate(self, request, context):
        solution = self.solve_quadratic(request.a, request.b, request.c)
        return quadratic_pb2.Solution(solution=solution)

    def CalculateStreamReply(self, request, context):
        for i in range(3):
            solution = self.solve_quadratic(request.a, request.b, request.c + i)
            yield quadratic_pb2.Solution(solution=solution)

    def CalculateBidiStream(self, request_iterator, context):
        for req in request_iterator:
            solution = self.solve_quadratic(req.a, req.b, req.c)
            yield quadratic_pb2.Solution(solution=solution)

    def solve_quadratic(self, a, b, c):
        discriminant = b ** 2 - 4 * a * c
        if discriminant > 0:
            root1 = (-b + discriminant ** 0.5) / (2 * a)
            root2 = (-b - discriminant ** 0.5) / (2 * a)
            return f"Roots are real and different: {root1}, {root2}"
        elif discriminant == 0:
            root = -b / (2 * a)
            return f"Roots are real and same: {root}"
        else:
            real_part = -b / (2 * a)
            imaginary_part = (-discriminant) ** 0.5 / (2 * a)
            return f"Roots are complex: {real_part} + {imaginary_part}i, {real_part} - {imaginary_part}i"

def serve():    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    quadratic_pb2_grpc.add_CalculateServicer_to_server(QuadraticCalculator(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started, listening on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
