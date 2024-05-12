# Name: Shawn Forrester
# Python 3.10.6
# client.py

#imports
import grpc
import quadratic_pb2
import quadratic_pb2_grpc

#run function to make the gRPC calls for each service.
def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = quadratic_pb2_grpc.CalculateStub(channel)

    # Unary RPC
    response = stub.Calculate(quadratic_pb2.QuadraticRequest(a=2, b=3, c=4))
    print("Unary RPC Result for equation 2x^2 + 3x + 4:", response.solution)

    # Server streaming RPC
    stream_response = stub.CalculateStreamReply(quadratic_pb2.QuadraticRequest(a=1, b=2, c=1))
    print("Server streaming RPC Result for equation x^2 + 2x + 1:")
    for sol in stream_response:
        print(sol.solution)

    # Bidirectional streaming RPC
    requests = [
        quadratic_pb2.QuadraticRequest(a=1, b=2, c=1),
        quadratic_pb2.QuadraticRequest(a=1, b=-2, c=1),
        quadratic_pb2.QuadraticRequest(a=1, b=0, c=-1)
    ]
    stream_response = stub.CalculateBidiStream(iter(requests))
    print("Bidirectional streaming RPC Result for x^2 + 2x + 1:")
    for sol in stream_response:
        print(sol.solution)

if __name__ == '__main__':
    run()
