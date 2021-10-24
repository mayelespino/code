#!/usr/bin/swift

struct Node {
    var Value: Character
    //var Prev: UnsafeMutablePointer<Node>!
    var Prev: Node?
    var Next: UnsafeMutablePointer<Node>!
    init(Value: Character){
        self.Value = Value
    }
}

var nodeA =  Node(Value: "a")
print (nodeA.Value)
var nodeB =  Node(Value: "b")
//nodeB.Prev = (UnsafeMutablePointer<Node>)&nodeA
var nodeC =  Node(Value: "c")
var nodeD =  Node(Value: "d")
