
package main

import (
	"fmt"
	"net/http"
	"io/ioutil"
)

func main() {
	http.HandleFunc("/",indexHandler)
	http.ListenAndServe(":8080",nil)
}

func indexHandler(resp http.ResponseWriter, req *http.Request) {
	filename:="login.html"
	body,err := ioutil.ReadFile(filename)
	if err != nil {
	    fmt.Fprintf(resp,"Load Index Page error")
        }
	fmt.Fprintf(resp,string(body))
}
