/*
 Using this app to find all keywords in go and generate 
*/
package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
)

func main() {
	fi, err := os.Open("io-demo.go")
	if err != nil {
		fmt.Println("Reading file occurs error")
		return
	}
	defer fi.Close()
	r := bufio.NewReader(fi)

	fo, err := os.OpenFile("output.txt",os.O_RDWR,0666)
	if err != nil {
		fmt.Println("Open file output.txt error")
		return
	}
	defer fo.Close()

	buf := make([]byte, 1024)
	for {
		n, err := r.Read(buf)
		if err != nil && err != io.EOF {
			fmt.Println("Reading error")
			break
		}
		if n == 0 {
			break
		}
		if nfo, err := fo.Write(buf[:n]); err != nil {
			fmt.Println(err)
			fmt.Println("Writing error")
			break
		} else if nfo != n {
			fmt.Println("Writing error")
			break
		}
	}
}
