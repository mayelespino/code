use std::collections::LinkedList;

fn merge_two_linked_list(list_a: LinkedList<u32>, list_b: LinkedList<u32>) -> LinkedList<u32> {
    let mut iter_a = list_a.iter().peekable();
    let mut iter_b = list_b.iter().peekable();

    let mut merged_list: LinkedList<u32> = LinkedList::new();


    loop {
        if iter_a.peek() ==  None || iter_b.peek() == None { break;}

        let value_a = **iter_a.peek().unwrap();
        let value_b = **iter_b.peek().unwrap();


        if  value_a < value_b {
            merged_list.push_back(value_a);
            iter_a.next();
        } else {
            merged_list.push_back(value_b);
            iter_b.next();
        }

    }

    for value in iter_a {
        merged_list.push_back(*value);
    }

    for value in iter_b {
        merged_list.push_back(*value);
    }

    return merged_list;

}

fn main() {

    let mut list_one: LinkedList<u32> = LinkedList::new();

    list_one.push_back(0);
    list_one.push_back(1);
    list_one.push_back(2);
    list_one.push_back(30);
    list_one.push_back(42);

    let mut list_two: LinkedList<u32> = LinkedList::new();
    list_two.push_back(10);
    list_two.push_back(11);
    list_two.push_back(13);
    list_two.push_back(14);
    list_two.push_back(19);
    list_two.push_back(20);
    list_two.push_back(21);

    let mut list_three: LinkedList<u32> = LinkedList::new();
    list_three.push_back(50);
    list_three.push_back(55);
    list_three.push_back(60);
    list_three.push_back(65);
    list_three.push_back(70);
    list_three.push_back(80);

    let mut merged_list = merge_two_linked_list(list_one, list_two);
    merged_list = merge_two_linked_list(merged_list, list_three);

    println!("Result:\n");

    for item in merged_list.iter(){
        println!("{}",item);

    }
}

// Links:
// https://doc.rust-lang.org/std/collections/struct.LinkedList.html
// https://doc.rust-lang.org/rust-by-example/flow_control/while.html
// https://web.mit.edu/rust-lang_v1.25/arch/amd64_ubuntu1404/share/doc/rust/html/reference/expressions/operator-expr.html
// https://rust-lang-nursery.github.io/rust-cookbook/algorithms/sorting.html
//https://doc.rust-lang.org/rust-by-example/std/option.html
// peekable: https://doc.rust-lang.org/nightly/std/iter/struct.Peekable.html