#!/usr/bin/swift 

import Foundation 
class MythicalBeast { 
    func whatsMyName() { 
        println("I don't know what I am, but I'm the stuff of legends.") 
    } 
} 

class Kraken: MythicalBeast { 
    override func whatsMyName() { 
        println("I'm the Kraken, yo!") 
    } 
} 

//can't use the Kraken class until after the declaration 
let kraken = Kraken() kraken.whatsMyName()

