/*
 package-description
*/
package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
)

func main() {
	readKeyWords("key.txt")
}

func readKeyWords(file string) {
	fi, err := os.Open(file)
	if err != nil {
		fmt.Println("Open file error")
		return
	}
	defer fi.Close()
	r := bufio.NewReader(fi)
	buf := make([]byte, 1024)
	str := ""
	for {
		n, err := r.Read(buf)
		if err != nil && err != io.EOF {
			fmt.Println("Reading file error")
			break
		}
		if n == 0 {
			break
		}
		//		fmt.Printf("Current len is %d",n)
		str = str + string(buf[:n])
	}
	//	fmt.Println(str)
	word := ""
	for _, char := range str {
		if char == 32 {
			if word != "" {
				println(word)
				word = ""
			}
		} else {
			word += string(char)
		}

	}

	//	println(' ')

}
