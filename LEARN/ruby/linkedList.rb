#!/usr/bin/ruby

class Node
  @previousNode = nil
  @nextNode = nil
  @value = nil
  
  def initialize(value)
    @value = value
  def insertInFront(node)
    @nextNode = node
    @nextNode.@previousNode = self

    
firstNode = Node.new(1)
    