extern crate rand;
use rand::Rng;

fn main() {
    println!("Merge sort");

    let mut rand_vector = generate_array();
    println!("Original: {:?}", rand_vector);
    println!("Sorted: {:?}", merge_sort(rand_vector));

}

fn generate_array() -> Vec<u8> {
    let mut rng = rand::thread_rng();

    let mut v : Vec<u8> = vec![0; 25 as usize];
    for x in v.iter_mut() {
        *x = rng.gen();
    }

    v
}

fn merge_sort(list: Vec<u8>) -> std::vec::Vec<u8> {
    if list.len() < 2 {
        return list;
    }

    let mid_point = list.len() / 2;
    let mut first_half = list;
    let second_half = first_half.split_off(mid_point);


    let mut right_vector = merge_sort(first_half);
    let mut left_vector = merge_sort(second_half);


    let mut merged_vector: Vec<u8> = Vec::new();
    while left_vector.len() > 0 && right_vector.len() > 0 {

        if left_vector[0] < right_vector[0] {
            let left_element = left_vector.remove(0);
            merged_vector.push(left_element);
        } else {
            let right_element = right_vector.remove(0);
            merged_vector.push(right_element);
        }

    }

    for element in left_vector{
        merged_vector.push(element);
    }

    for element in right_vector {
        merged_vector.push(element);
    }

    merged_vector

}