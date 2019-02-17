# How to start

## Setup python dev environment

```
$ python3 -m venv venv
$ source venv/bin/activate
```

## Setup for gPRC project

```
$ python -m pip install --upgrade pip
$ python -m pip install grpcio
$ python -m pip install grpcio-tools
 ```

## Bring the proto file `./route_guide.proto`

## Generate Python codes from the proto file

```
$ python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./route_guide.proto
```

# How to run

### Run server (Go implementation). Check [here](https://github.com/momotaro98/go-codes-for-learning/tree/master/grpc-tutorial-routeguide).

```
$ cd go-codes-for-learning/grpc-tutorial-routeguide
$ go run server/server.go -port 50051
```

### Run client

```
$ python route_guide_client.py
```
