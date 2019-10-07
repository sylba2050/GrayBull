package main

import (
	"flag"
	"fmt"

	"github.com/kkdai/youtube"
)

func main() {
	flag.Parse()

	y := youtube.NewYoutube(false)

	arg := flag.Arg(0)

	if err := y.DecodeURL(arg); err != nil {
		fmt.Println("err:", err)
	}
	if err := y.StartDownload("dl.mp4"); err != nil {
		fmt.Println("err:", err)
	}
}
