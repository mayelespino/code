/**
 * Created by mayelespino on 1/22/18.
 */
/**
 * From Derek Banas' Kotlin Tutorial: https://youtu.be/H_oGi8uuDpA
 */
package demo
import java.util.Random

fun main(srgd: Array<String>){
    println("T01 Demo.")
    var biggestInt: Int = Int.MAX_VALUE
    var smallestInt: Int = Int.MIN_VALUE
    println("Biggest : "+ biggestInt)
    println("Smallets: $smallestInt")
    // Can do the same for Long, Double, Float, Boolean, Short, Byte ...

    //==============================================================

    println("3.1416 to Int:" +(3.1416.toInt()))
    println("A to Int: " + ('A'.toInt()))
    println("65 to Char:" + (65.toChar()))

    //==============================================================

    val longString = """
This is a test
of a multi-line
string
"""
    println(longString)

    var s1 = "A random string"
    var s2 = "a random string"
    println("are s1 and s2 equal?: ${s1.equals(s2)}")
    println("Compare s1 to s2: ${s1.compareTo(s2)}")
    println("Index 2: ${s1[2]}")
    println("sub 1-7: ${s1.subSequence(2,8)}")
    println("Contains random: ${s1.contains("random")}")

    //==============================================================
    var myArray = arrayOf(1, 1.23, "Doug")
    println(myArray[2])
    myArray[1] = 3.1416
    println("MyArray length ${myArray.size}")
    println("MyArray contain Doug ${myArray.contains("Doug")}")
    var partialArray = myArray.copyOfRange(0,1)
    println("First in partialArray ${partialArray.first()}")
    println("Dough index: ${myArray.indexOf("Doug")}")
    //
    var sqrArray = Array(5,{x-> x*x})
    println(sqrArray[2])
    //
    var intArray: Array<Int> = arrayOf(1,2,3)

    //==============================================================
    val numRange = 0..10
    val alpha = "A".."Z"
    println("R in alpha: ${"R" in alpha}")

    val tenTo1 = 10.downTo(1)
    val twoTo20 = 2.rangeTo(20)
    val range3 = numRange.step(3)
    for(x in range3) println("range3: $x")
    for(x in range3.reversed()) println("reversed range3: $x")

    //==============================================================
    /*
        if( age < 5){
           println("goto preschool")
        } else if (age == 5) {
           println("goto kinder")
        } else {
           println("goto school")
        }
     */

//    when(age){
//        0,1,2,3,4 -> println("Goto preschool")
//
//        5 -> println("Goto kinder")
//
//        in 6-17 ->{
//            val grade = age - 5
//            println("grade: $grade")
//        }
//
//        else -> println("Goto school")
//    }

    //=============================================================
    val rand = Random()
    val magicNumber = rand.nextInt(50) + 1
    var guess = 0

    while(magicNumber != guess){
        guess += 1
    }
    println("guess : $guess")

    // There is continue and break for loops

    var arr3: Array<Int> = arrayOf(3,6,9)
    for(i in arr3.indices){
        println("arr3: ${arr3[i]}")
    }

    for((index, value) in arr3.withIndex()){
        println("Index: $index Value: $value")
    }

    for(a in arr3){
        println("arr3: $a")
    }

    //=============================================================
    fun add(num1: Int = 0, num2: Int) : Int = num1 + num2
    println("1+1: ${add(1,1)}")

    fun sayHi(name: String): Unit = println("Hello $name")
    sayHi("Jon")

    val (two,three) = nextTwo(1)
    println("1 $two $three")

    println("Sum(1,2,3,4,5): ${getSum(1,2,3,4,5)}")

    val multiply = {num1:Int, num2: Int -> num1 * num2}
    println("5*3 = ${multiply(5, 3)}")

    println("5! = ${fact(5)}")

    //=============================================================
    var numList = 1..20
    val evenList = numList.filter{it %2 == 0}
    evenList.forEach{n-> println(n)}
    //
    val mul3 = makeMathFunc(3)
    println("5*3 = ${mul3(5)}")

    val multiply2 = {num1: Int -> num1 * 2}
    val numberList2 = arrayOf(1,2,3,4,5)

    mathOnList(numberList2, multiply2)

    //=============================================================
    val numList3 = 1..20
    val listSum = numList3.reduce{x, y -> x + y}
    println("listSum: $listSum")
    val listFold = numList3.fold(5){x, y -> x + y}
    println("listFold: $listFold")
    //
    println("Even nums: ${numList3.any{it % 2 == 0}}")
    println("Even nums: ${numList3.all{it % 2 == 0}}")
    val grater3 = numList3.filter { it > 3 }
    grater3.forEach{ n -> println("$n > 3")}
    val times7 = numList3.map{ it * 7}
    times7.forEach{n -> println("times7: $n")}

    //=============================================================
    var mutList: MutableList<Int> = mutableListOf(1,2,3,4,5)
    // There is also inmuttable lists
    mutList.add(6)
    println("first: ${mutList.first()}")
    println("Last: ${mutList.last()}")
    println("Size: ${mutList.size}")
    //mutList.clear() you can also clear inmuttable lists
    println("------------")
    mutList.forEach{ n-> println("mutList: $n ")}
    println("------------")
    mutList.remove(2)
    mutList.forEach{ n-> println("mutList: $n ")}
    println("------------")
    mutList.removeAt(2)
    mutList.forEach{ n-> println("mutList: $n ")}

    //=============================================================
    var map = mutableMapOf<Int, Any?>()
    map[1] = "Doug"
    map[2] = 2
    println("map size: ${map.size}")

    map.put(3, "California")
    map.remove(2)

    for((key, value) in map){
        println("K;$key V:$value")
    }


}

fun nextTwo(num: Int): Pair<Int, Int>{
    return Pair(num+1, num+2)
}

fun getSum(vararg numbers: Int): Int{
    var sum = 0

    numbers.forEach { n-> sum += n }
    return(sum)
}

fun fact(num: Int): Int{
    tailrec fun factTail(y: Int, z: Int): Int{
        if(y == 0) return z
        else return factTail(y-1, y*z)
    }
    return factTail(num, 1)
}

fun makeMathFunc(num1: Int): (Int) -> Int = {num2 -> num1 * num2}

fun mathOnList(numList: Array<Int>, myFunc: (num: Int) -> Int){
    for(num in numList){
        println("MathOnList: ${myFunc(num)}")
    }
}