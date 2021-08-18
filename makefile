proto: fetch.proto kinova.proto
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. fetch.proto
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. kinova.proto
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. webapp.proto
