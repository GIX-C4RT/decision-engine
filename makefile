proto: fetch.proto kinova.proto
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. fetch.proto
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. kinova.proto
