/**
 * Created by mayelespino on 1/24/18.
 */
package demo

fun main(args: Array<String>){

    val bowser = Animal("Bowser", 20.0, 13.5)
    bowser.getInfo()

    val myDog = Dog("ppk", 10.0, 5.0, "Me")
    myDog.getInfo()

    val myBird = Bird("Tweety", true)
    myBird.fly(20.0)

}

open class Animal (val name: String,
                   var height: Double,
                   var weight: Double) {
    init{
        val regex = Regex(".*\\d+.*")

        require(!name.matches(regex)) {"Name can not have number."}
        require(height > 0) {"heigth can not be 0 "}
        require(weight > 0) {"weigth can not be 0 "}
    }

    open fun getInfo(): Unit
    {
        println("name: $name height: $height  weight: $weight")
    }

}

class Dog ( name: String,
            height: Double,
            weight: Double,
           var owner: String) : Animal(name, height, weight){
    override fun getInfo() : Unit {
        println("name: $name height: $height  weight: $weight owner: $owner")
    }
}


interface Flyable {
    var flies: Boolean
    fun fly(distance: Double): Unit
}

class Bird constructor(val name: String,
                       override var flies: Boolean = true
) : Flyable{
    override fun fly(distance: Double): Unit {
        if(flies){
            println("$name flew: $distance miles")
        }
    }
}