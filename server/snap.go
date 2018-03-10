package main

import (
	"io/ioutil"
	"log"
	"net"

	"golang.org/x/net/context"

	pb "github.com/mellowdrifter/snapshot/proto"

	"google.golang.org/grpc"
)

type server struct{}

func main() {
	log.Println("Listening on port 5001")
	lis, err := net.Listen("tcp", ":5001")
	if err != nil {
		log.Fatalf("Failed to bind: %v,", err)
	}

	grpcServer := grpc.NewServer()
	pb.RegisterSnapShotServer(grpcServer, &server{})

	grpcServer.Serve(lis)
}

func (s *server) AddSnap(ctx context.Context, id *pb.ImageData) (*pb.Result, error) {
	log.Printf("Received an image from the camera in location %v", id.GetLocation())
	err := ioutil.WriteFile("test.jpg", id.GetImage(), 0644)
	if err != nil {
		log.Fatalf("Cannot write file")
	}
	return &pb.Result{
		Reply: "I got something",
	}, nil
}
