import sys
sys.path.append('generated')
import zkp_pb2
from zkp_pb2_grpc import ZKPProtocolServicer


class ZKPProtocolServicer(zkp_pb2_grpc.ZKPProtocolServicer):
    def Register(self, request, context):
        x = request.x
        y1 = pow(g, x, p)
        y2 = pow(h, x, p)
        return zkp_pb2.RegistrationResponse(y1=y1, y2=y2)

    def Authenticate(self, request, context):
        c = request.c
        s = request.s
        v1 = pow(g, s, p)
        v2 = pow(h, c, p) * pow(y1, s, p)
        v3 = pow(h, s, p)
        if v1 == v2:
            return zkp_pb2.AuthenticationResponse(success=True)
        else:
            return zkp_pb2.AuthenticationResponse(success=False)

if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    zkp_pb2_grpc.add_ZKPProtocolServicer_to_server(ZKPProtocolServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
