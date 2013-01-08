package main

import "os"

func main() {
	buf := make([]byte, 1024)
	f, _ := os.Open("demo1.go")
	defer f.Close()
	for {
		n, _ := f.Read(buf)
		if n == 0 {
			break
		}
		os.Stdout.Write(buf[:n])
	}

}

func hello(x int) int {
}

