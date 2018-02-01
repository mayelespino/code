/**
 * Created by mayelespino on 1/26/18.
 */
package code

//import kotlin.math.*
import java.util.*

// Node data class
data class Node(var int_value: Int, var right: Node?, var left: Node?)


fun add_node(current:Node, int_add: Int) {
    //var current: Node = root

    if (int_add > current.int_value && current.right != null) {
        current.right?.let {
            add_node(current.right, int_add)
        }
    } else if (int_add > current.int_value && current.right == null) {
        //var new_node = Node(int_add, null, null)
        current.right = Node(int_add, null, null)
    }
}

fun add_nodes_random(root:Node)
{

    for(i in 1..20) {
        var next_int = Random().nextInt(99)
        add_node(root, next_int)
    }

}
fun main(args: Array<String>){
    var root = Node(5, null, null)

    add_nodes_random(root)
}