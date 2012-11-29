package main

import "fmt"

func main() {
  fmt.Printf("Hello, Go world")
  
  if true && true {
     fmt.Println("True")
  }
  
  sum := 0
  for i := 0;i<10;i++ {
      sum+=i
  }
  fmt.Println(sum)

  println("heee")

		list := []string{"a","b","c"}
	for k,v := range list{
		fmt.Printf("K is %d, V is %s \n",k,v)
	}


}

func myfunc() {
  i := 0
  println(i)
  i++
}
