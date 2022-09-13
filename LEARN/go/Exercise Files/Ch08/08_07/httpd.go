// Key/Value database
package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"sync"
)

var (
	db     = map[string]interface{}{}
	dbLock sync.Mutex
)

// Entry is a map entry, fits both request and response
type Entry struct {
	Key   string      `json:"key"`
	Value interface{} `json:"value"`
}

func sendResponse(entry *Entry, w http.ResponseWriter) {
	w.Header().Set("Content-Type", "application/json")
	enc := json.NewEncoder(w)
	if err := enc.Encode(entry); err != nil {
		log.Printf("error encoding %+v - %s", entry, err)
	}
}

func kvPostHandler(w http.ResponseWriter, r *http.Request) {
	// Decode request
	defer r.Body.Close()
	dec := json.NewDecoder(r.Body)
	entry := &Entry{}
	if err := dec.Decode(entry); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	// Do work
	dbLock.Lock()
	defer dbLock.Unlock()
	db[entry.Key] = entry.Value

	// Encode response
	sendResponse(entry, w)
}

func kvGetHandler(w http.ResponseWriter, r *http.Request) {
	// GET /<key>
	key := r.URL.Path[4:] // Trim leading /db/ prefix

	// Do work
	dbLock.Lock()
	defer dbLock.Unlock()

	value, ok := db[key]
	if !ok {
		http.Error(w, fmt.Sprintf("Key %q not found", key), http.StatusNotFound)
		return
	}

	// Encode response
	entry := &Entry{
		Key:   key,
		Value: value,
	}
	sendResponse(entry, w)
}

func main() {
	http.HandleFunc("/db", kvPostHandler)
	http.HandleFunc("/db/", kvGetHandler)
	if err := http.ListenAndServe(":8080", nil); err != nil {
		log.Fatal(err)
	}
}
