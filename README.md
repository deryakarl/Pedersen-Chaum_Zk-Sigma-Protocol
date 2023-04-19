# Pedersen-Chaum Protocol 
Simple implemention of a Zero-Knowledge Proof (ZKP) protocol for 1-factor authentication. The protocol should support the registration and login processes, where the prover (client) has a secret password x, and the verifier (server) verifies the authentication check.
# Implement the gRPC server and client 
 run the command to generate Python code from the zkp.proto
 
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. zkp.proto

 This will generate zkp_pb2.py and zkp_pb2_grpc.py 
# Run in different terminals

python server.py

python client.py
