

Go Notes 


Go is a compiled language. Which means that it is only compiled once(Or when needed to be compiled). This is opposed to
interpreted langues like python which need to be compiled (Converted to Machine language) each time it is run. 



package main lets the Go compiler know that we want this code to compile and run as a standalone program, as opposed to
being a library that's imported by other programs.

import fmt imports the fmt (formatting) package. The formatting package exists in Go's standard library and lets us do things
like print text to the console.

func main() defines the main function. main is the name of the function that acts as the entry point for a Go program.


Memory Management 

Memory Management is covered by an appended piece of code called Go Runtime



Data Types: 

bool

string

int  int8  int16  int32  int64
uint uint8 uint16 uint32 uint64 uintptr

byte // alias for uint8

rune // alias for int32
     // represents a Unicode code point

float32 float64

complex64 complex128



Variable Decleration 

Variables are declared using the following syntax: 

var myVariable Type(String,int) 

Short variables can be declared simply: 

myVariable := 4




variable types can also be inferred by using the following syntax: 

myVariable := 6 

Multiple Variables can be declared in the same line by using the following syntax 

var1, var2 := 123, "Hello"



Constants 

Constants can not use the short decleration, it must be defined as a constant 

const myConstant = 4 

you can also compute constants, for example: 


const firstName = "Lane"
const lastName = "Wagner"
const fullName = firstName + " " + lastName





Formatting Strings 

fmt.Printf - Prints formatted string to standard out 
fmt.Sprintf() - Returns a formatted string 
