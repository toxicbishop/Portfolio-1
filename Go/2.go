package main

import (
	"bytes"
	"encoding/binary"
	"fmt"
	"os"
)

const (
	PageSize = 32 * 1024        // 32 KB
	DiskSize = 10 * 1024 * 1024 // 10 MB
	NumPages = DiskSize / PageSize
	MaxFiles = 5
	NameSize = 100 // fixed length for file names
)

// FileEntry is the metadata stored in the header
type FileEntry struct {
	Name   string
	Start  int64 // start page index
	Pages  int64 // number of pages occupied
	Length int64 // actual length in bytes
}

// Page-based disk abstraction
type Disk struct {
	pages [][]byte
}

// Create a new blank disk
func NewDisk() *Disk {
	d := &Disk{pages: make([][]byte, NumPages)}
	for i := range d.pages {
		d.pages[i] = make([]byte, PageSize)
	}
	return d
}

// Write a full page
func (d *Disk) WritePage(pageIndex int64, data []byte) {
	copy(d.pages[pageIndex], data)
}

// Read a full page
func (d *Disk) ReadPage(pageIndex int64) []byte {
	return d.pages[pageIndex]
}
func main() {
	// Step 1: Create disk
	disk := NewDisk()

	// Step 2: Example file contents
	files := [][]byte{
		[]byte("This is file 1 data."),
		[]byte("This is file 2 data."),
		[]byte("This is file 3 data."),
		[]byte("This is file 4 data."),
		[]byte("This is file 5 data."),
	}
	names := []string{"file1.txt", "file2.txt", "file3.txt", "file4.txt", "file5.txt"}
	// Step 3: Store files page by page
	var entries []FileEntry
	currentPage := int64(1) // page 0 reserved for header
	for i := 0; i < MaxFiles; i++ {
		data := files[i]
		pagesNeeded := (len(data) + PageSize - 1) / PageSize
		// Write file data page by page
		for p := 0; p < pagesNeeded; p++ {
			start := p * PageSize
			end := start + PageSize
			if end > len(data) {
				end = len(data)
			}
			chunk := make([]byte, PageSize)
			copy(chunk, data[start:end])
			disk.WritePage(currentPage+int64(p), chunk)
		}
		entries = append(entries, FileEntry{
			Name:   names[i],
			Start:  currentPage,
			Pages:  int64(pagesNeeded),
			Length: int64(len(data)),
		})
		currentPage += int64(pagesNeeded)
	}
	// Step 4: Write header into page 0
	header := new(bytes.Buffer)
	for _, e := range entries {
		nameBytes := make([]byte, NameSize)
		copy(nameBytes, []byte(e.Name))
		header.Write(nameBytes)
		binary.Write(header, binary.LittleEndian, e.Start)
		binary.Write(header, binary.LittleEndian, e.Pages)
		binary.Write(header, binary.LittleEndian, e.Length)
	}
	// Pad header to page size
	hdrPage := make([]byte, PageSize)
	copy(hdrPage, header.Bytes())
	disk.WritePage(0, hdrPage)
	// Step 5: Save entire disk to file
	f, _ := os.Create("page_disk.bin")
	defer f.Close()
	for _, pg := range disk.pages {
		f.Write(pg)
	}
	fmt.Println("Disk saved with 32KB paging.")
	// ------------------------
	// READING BACK
	// ------------------------
	// Step 6: Load disk back
	raw, _ := os.ReadFile("page_disk.bin")
	readDisk := &Disk{pages: make([][]byte, NumPages)}
	for i := 0; i < NumPages; i++ {
		readDisk.pages[i] = make([]byte, PageSize)
		copy(readDisk.pages[i], raw[i*PageSize:(i+1)*PageSize])
	}
	// Step 7: Parse header (page 0)
	headerPage := readDisk.ReadPage(0)
	reader := bytes.NewReader(headerPage)
	var readEntries []FileEntry
	for i := 0; i < MaxFiles; i++ {
		nameBytes := make([]byte, NameSize)
		reader.Read(nameBytes)
		var start, pages, length int64
		binary.Read(reader, binary.LittleEndian, &start)
		binary.Read(reader, binary.LittleEndian, &pages)
		binary.Read(reader, binary.LittleEndian, &length)
		if start == 0 && pages == 0 && length == 0 {
			continue
		}
		name := string(bytes.Trim(nameBytes, "\x00"))
		readEntries = append(readEntries, FileEntry{Name: name, Start: start, Pages: pages, Length: length})
	}
	// Step 8: Print recovered files + Page Map
	fmt.Println("\nRecovered Files:")
	for _, e := range readEntries {
		var data []byte
		for p := int64(0); p < e.Pages; p++ {
			page := readDisk.ReadPage(e.Start + p)
			data = append(data, page...)
		}
		data = data[:e.Length] // trim padding
		fmt.Printf("File: %s (Pages %d–%d)\nData: %s\n\n",
			e.Name, e.Start, e.Start+e.Pages-1, string(data))
	}
	// Step 9: Print Page Map
	fmt.Println("Page Map (total", NumPages, "pages):")
	fmt.Println("[0] HEADER")
	usedUntil := int64(0)
	for _, e := range readEntries {
		fmt.Printf("[%d-%d] %s\n", e.Start, e.Start+e.Pages-1, e.Name)
		if e.Start+e.Pages-1 > usedUntil {
			usedUntil = e.Start + e.Pages - 1
		}
	}
	if usedUntil < NumPages-1 {
		fmt.Printf("[%d-%d] FREE\n", usedUntil+1, NumPages-1)
	}
}
