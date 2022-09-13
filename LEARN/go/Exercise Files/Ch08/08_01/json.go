// JSON example
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"log"
)

var data = `
{
  "user": "Scrooge McDuck",
  "type": "deposit",
  "amount": 1000000.3
}
`

// Request is a bank transactions
type Request struct {
	Login  string  `json:"user"`
	Type   string  `json:"type"`
	Amount float64 `json:"amount"`
}

func main() {
	rdr := bytes.NewBufferString(data) // Simulate a file/socket

	// Decode request
	dec := json.NewDecoder(rdr)

	req := &Request{}
	if err := dec.Decode(req); err != nil {
		log.Fatalf("error: can't decode - %s", err)
	}

	fmt.Printf("got: %+v\n", req)
}
	