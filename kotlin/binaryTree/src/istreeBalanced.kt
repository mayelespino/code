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

    fun dept(): Int? {
        var dept_right: Int? = 0
        var dept_left: Int? = 0
        if (right != null){
            dept_right = right?.dept()
            if(dept_right != null) {dept_right += 1}
         } else {
            dept_right = 1
        }

        if (left != null){
            dept_left = left?.dept()
            if(dept_left != null) {dept_left += 1}
        } else {
                dept_left = 1
        }

        var return_value = 0
        if(dept_left != null && dept_right != null) {
            if (dept_left > dept_right) {
                return_value = dept_left
            } else {
                return_value = dept_right
            }
        }
        return (return_value)
    }

    fun isBalanced(): Boolean {
        var dept_right: Int? = 0
        var dept_left: Int? = 0

        if (right != null){
            dept_right = right?.dept()
        } else {
            dept_right = 0
        }

        if (left != null){
            dept_left = left?.dept()
        } else {
            dept_left =  0
        }

        var difference = 0
        if(dept_left != null && dept_right != null) {
            difference = dept_left - dept_right
        }

        if( difference > 0 && difference <= 1 ) {
            return true
        }
        return false
    }
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
    println("\n dept")
    val right_depth = root.right?.dept()
    val left_depth = root.left?.dept()
    println(right_depth)
    println(left_depth)
}