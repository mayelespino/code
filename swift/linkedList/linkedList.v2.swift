#!/usr/bin/swift
import Foundation

public class Node {
    public var value: String
    public var next: Node?
    public weak var prev: Node?
    
    public init(value: String) {
        self.value = value
        self.next =  nil
        self.prev = nil
    }
}

public class linkedList {
    var start: Node?
    var end: Node?
    public init(start: Node){
        self.start = start
        self.end = start
    }
    public func printList()
    {
        var iterator = self.start
        if iterator ==  nil {return}
        var value = iterator?.value
        while iterator != nil{
            print(value as Any)
            print("next")
            iterator = iterator?.next
            value = iterator?.value
        }
    }
}

let node1 = Node(value:"one")
let node2 = Node(value:"two")
node2.prev = node1
let node3 = Node(value:"three")
node3.prev = node3
node2.next = node3
let node4 = Node(value:"four")
node4.prev = node3
node3.next = node4

let list = linkedList(start:node1)
list.printList()

