package main

import (
	"fmt"
)

const (
	PageSize    = 10 * 1024 * 1024 // 10 MiB in bytes
	ChunkSize   = 32 * 1024        // 32 KiB in bytes
	TotalChunks = PageSize / ChunkSize
)

func main() {
	// Create the page (10 Mib size page)
	page := make([]byte, PageSize)

	fmt.Printf("Page size: %d bytes\n", PageSize)
	fmt.Printf("Chunk size: %d bytes\n", ChunkSize)
	fmt.Printf("Total chunks: %d\n", TotalChunks)

	// store data into a specific chunk
	data := []byte("Hello from Chunk 5!")
	chunkIndex := 16

	// Calculate the offset in bytes
	start := chunkIndex * ChunkSize
	end := start + len(data)

	copy(page[start:end], data)

	// Read back the data from the same chunk
	readData := page[start : start+len(data)]
	fmt.Printf("Read from chunk %d: %s\n", chunkIndex, string(readData))
}
