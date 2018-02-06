/**
 * Created by mayelespino on 1/26/18.
 */
package code

//import kotlin.math.*
import java.util.*

// Node data class
data class Node(val int_value: Int, var right: Node? = null, var left: Node? = null){
    fun add(int_to_add: Int){
        if (int_to_add >= int_value) {
            if(right != null) {
                right?.add(int_to_add)
            } else {
                var new_node = Node(int_to_add, null, null)
                right = new_node
            }
        } else {
            if(left != null) {
                left?.add(int_to_add)
            } else {
                var new_node = Node(int_to_add, null, null)
                left = new_node
            }
        }
    }
    override fun toString() = " $int_value"
    fun preOrder()  { print(this); left?.preOrder(); right?.preOrder() }
    fun inorder()   { left?.inorder(); print(this); right?.inorder() }
    fun postOrder() { left?.postOrder(); right?.postOrder(); print(this) }
}

fun main(args: Array<String>){


    var root = Node(5, null, null)

    for(i in 1..20) {
        var next_int = Random().nextInt(99)
        root.add(next_int)
    }

    println("pre order")
    root.preOrder()
    println("\n in order")
    root.inorder()
    println("\n post order")
    root.postOrder()
}