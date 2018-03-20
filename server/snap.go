package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net"
	"os"
	"time"

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
	log.Printf("Received an image from the camera in location %v and sequence %v", id.GetLocation(), id.GetSequence())
	date := time.Unix(int64(id.GetDateTime()), 0)
	folder := fmt.Sprintf("%v/%v/%v", "/home/fujitsu/snap", id.GetLocation(), date.Format("2006-01-02"))
	if _, err := os.Stat(folder); os.IsNotExist(err) {
		os.MkdirAll(folder, os.ModePerm)
	}
	filename := fmt.Sprintf("%v/%v.jpg", folder, id.GetSequence())
	err := ioutil.WriteFile(filename, id.GetImage(), 0666)
	if err != nil {
		log.Fatalf("Cannot write file")
	}
	return &pb.Result{
		Reply: "I got something",
	}, nil
}
