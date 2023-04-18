import grpc
import zkp_pb2
import zkp_pb2_grpc

def register(stub, x, g, h):
    # Calculate y1 and y2 using x, g, and h
    y1 = g ** x
    y2 = h ** x

    # Send y1 and y2 to the server for registration
    request = zkp_pb2.RegistrationRequest(y1=y1, y2=y2)
    response = stub.Register(request)
    return response.success

def authenticate(stub, y1, y2, c, s, g, h):
    # Step 1: Prover selects a random r and computes a = g^r and b = h^r
    r = 12345 # replace with a random number
    a = g ** r
    b = h ** r

    # Step 2: Prover sends a and b to the Verifier
    request = zkp_pb2.AuthenticationRequest(a=a, b=b)
    response = stub.Authenticate(request)

    # Step 3: Verifier sends a random challenge c to Prover
    # Step 4: Prover sends s = r + cx to Verifier
    # Step 5: Verifier checks that a^c * y1^s == b^c * y2^s
    if response.challenge == c:
        s = r + c * x
        left_hand_side = (a ** c) * (y1 ** s)
        right_hand_side = (b ** c) * (y2 ** s)
        if left_hand_side == right_hand_side:
            return True

    return False

if __name__ == '__main__':
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = zkp_pb2_grpc.ZKPProtocolStub(channel)

        # Public parameters
        g = 5
        h = 7

        # Registration process
        x = 12345
        success = register(stub, x, g, h)
        print('Registration success:', success)

        # Login process
        c = 67890
        s = 54321
        success = authenticate(stub, g, h, c, s, g, h)
        print('Authentication success:', success)
