package main

import ("fmt"
)

type Node struct{
	left,right,point int
	next *Node
}

type ExamRoom struct {
	head *Node
	caddMap map[int]*Node
}


func Constructor(N int) ExamRoom {
	var start = Node{0,N,0,nil}
	var end = Node{N,0,N-1,nil}
	var map1 = make(map[int]*Node)
	map1[0] = &start
	map1[N-1] = &end
	start.next = &end
	var room = ExamRoom{&start,map1}
	room.head.next = &end
	return room
}

func getValue(node *Node)int{
	if node.left == 0{
		return node.right
	}
	if node.right ==0{
		return node.left
	}
	if node.left > node.right{
		return node.right
	}else{
		return node.left
	}
}

func (this *ExamRoom) Seat() int {
	var maxV =0
	var tmp = 0
    for k,_ := range this.caddMap{
		if getValue(this.caddMap[k]) > maxV{
			maxV = getValue( this.caddMap[k])
			tmp = k
		}
	}
}


func (this *ExamRoom) Leave(p int)  {
    
}


/**
 * Your ExamRoom object will be instantiated and called as such:
 * obj := Constructor(N);
 * param_1 := obj.Seat();
 * obj.Leave(p);
 */


 
func main() {
	var ls = []int{36,74,84,92,17,68,97,6,68,85}
	fmt.Println(sumSubarrayMins(ls))
}
