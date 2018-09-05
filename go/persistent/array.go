package main

import ("fmt"
	 "math"
	 "github.com/stretchr/testify/assert")

type Tree struct{
	Value int
	Left *Tree
	Right *Tree
}

type PersistentArray struct{
	LastUsed int
	Pool []Tree
	L int 
	R int
}

func(array *PersistentArray) GetNewNode() *Tree {
	var lastused = array.LastUsed
	array.LastUsed += 1
	return &array.Pool[lastused]
}

func(array *PersistentArray) get(v *Tree ,l int,r int, at int,val int) *Tree{
	var res = array.GetNewNode()
	
	if( v != nil){
		*res = * v
	}

	if(l +1 == r){
		
	}

	return res
}

func main() {
	var LEN = 20* math.Pow(10,6)
	fmt.Println(LEN)
	var pool [20000000]Tree
	fmt.Println(pool[0].Value)
	fmt.Println(pool[19999999].Value)
	fmt.Println(pool[19999999].Left)
	var t = &Tree{10,nil,nil}
	fmt.Println(t.Value)
}