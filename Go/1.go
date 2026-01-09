package main

import (
	"bytes"
	"encoding/binary"
	"fmt"
	"os"
)

const (
	// PageSize removed to avoid redeclaration error
	DiskSize   = 10 * 1024 * 1024 // 10 MiB
	MaxFiles   = 5
	NameSize   = 100                           // fixed name size (bytes)
	HeaderSize = MaxFiles * (NameSize + 8 + 8) // name + offset + length
)

type FileEntry struct {
	Name   string
	Offset int64
	Length int64
}

func main() {
	// Step 1: Create "disk" in memory
	disk := make([]byte, DiskSize)
	// Step 2: Prepare files to store
	fileData := [][]byte{
		[]byte("This is file 1 data."),
		[]byte("This is file 2 data."),
		[]byte("This is file 3 data."),
		[]byte("This is file 4 data."),
		[]byte("This is file 5 data."),
	}
	fileNames := []string{"file1.txt", "file2.txt", "file3.txt", "file4.txt", "file5.txt"}
	// Step 3: Write files into disk
	var entries []FileEntry
	offset := int64(HeaderSize) // leave space for file table
	for i := 0; i < MaxFiles; i++ {
		copy(disk[offset:], fileData[i])
		entries = append(entries, FileEntry{
			Name:   fileNames[i],
			Offset: offset,
			Length: int64(len(fileData[i])),
		})
		offset += int64(len(fileData[i]))
	}
	// Step 4: Write file table into disk header
	header := new(bytes.Buffer)
	for _, e := range entries {
		nameBytes := make([]byte, NameSize)
		copy(nameBytes, []byte(e.Name))
		header.Write(nameBytes)
		binary.Write(header, binary.LittleEndian, e.Offset)
		binary.Write(header, binary.LittleEndian, e.Length)
	}
	copy(disk, header.Bytes())
	// Step 5: Save disk to file
	err := os.WriteFile("virtual_disk.bin", disk, 0644)
	if err != nil {
		panic(err)
	}
	fmt.Println("Disk created and files written.")
	// Step 6: Read disk from file
	readDisk, err := os.ReadFile("virtual_disk.bin")
	if err != nil {
		panic(err)
	}
	// Step 7: Parse header and read back files
	reader := bytes.NewReader(readDisk)
	var readEntries []FileEntry
	for i := 0; i < MaxFiles; i++ {
		nameBytes := make([]byte, NameSize)
		reader.Read(nameBytes)
		var offset, length int64
		binary.Read(reader, binary.LittleEndian, &offset)
		binary.Read(reader, binary.LittleEndian, &length)
		name := string(bytes.Trim(nameBytes, "\x00"))
		readEntries = append(readEntries, FileEntry{Name: name, Offset: offset, Length: length})
	}
	// Step 8: Display files read back
	for _, e := range readEntries {
		data := readDisk[e.Offset : e.Offset+e.Length]
		fmt.Printf("File: %s\nData: %s\n", e.Name, string(data))
	}
}
