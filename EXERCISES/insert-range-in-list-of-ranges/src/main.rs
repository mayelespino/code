// Given a sorted list of distinct ranges, write a function that will insert a new range
// to the list such that you have a new sorted list of distinct ranges.
// Ranges that overlap must be merged together to preserve distinctness.
//

// Examples:
//
// insertRange([7, 9], [[1, 2], [3, 5],[12, 15]])
// => [[1, 2], [3, 5], [7, 9], [12, 15]]
//
// insertRange([2, 4], [[1, 2], [3, 5], [12, 15]])
// => [[1, 5], [12, 15]]


fn inset_range(range_to_insert: [u8; 2], original_range: &mut Vec<[u8;2]>)  {

    // println!("array is {:?} original range {:?}",range_to_insert, original_range);
    // Two special cases, insert at the start, and at the end
    if range_to_insert[1] < original_range[0][0] {
        original_range.insert(0,range_to_insert);
        return;

    } else if range_to_insert[0] > original_range[original_range.len()-1][0] {
        original_range.push(range_to_insert);
        return;
    }

    let mut new_element : [u8; 2] = [0;2];
    let mut new_location : usize = 0;
    let mut is_merge : bool = false;
    let mut is_link_merge : bool = false;

    for ( location,  element) in  original_range.iter().enumerate() {

        if range_to_insert[0] < element[0] && range_to_insert[1] < element[0] {
            new_location = location;
            break;
        } else if range_to_insert[0] >= original_range[location][0] && range_to_insert[0] <= original_range[location][1] && range_to_insert[1] >= original_range[location+1][0] &&  range_to_insert[1] <= original_range[location+1][1] {
            new_location = location;
            is_link_merge = true;

            new_element[0] = original_range[location][0];
            new_element[1] = original_range[location+1][1];
            break;
        } else if range_to_insert[0] >= element[0] && range_to_insert[0] <= element[1] || range_to_insert[1] >= element[0] &&  range_to_insert[1] <= element[1] {
            new_location = location;
            is_merge = true;

            if range_to_insert[0] < element[0]{
                new_element[0] = range_to_insert[0];
            } else {
                new_element[0] = element[0];
            }

            if range_to_insert[1] > element[1] {
                new_element[1] = range_to_insert[1];
            } else {
                new_element[1] = element[1];
            }

            break;
        } // if
    } // for

    if is_merge == false && is_link_merge == false {
        original_range.insert(new_location, range_to_insert);
    } else if is_merge == true && is_link_merge ==  false {
        original_range.remove(new_location);
        original_range.insert(new_location, new_element);
    } else if is_merge == false && is_link_merge == true{
        original_range.remove(new_location);
        original_range.remove(new_location);
        original_range.insert(new_location, new_element);
    }


}

fn main() {

    let vector: &mut Vec<[u8;2]> = &mut vec![];
    vector.push([1, 2]);
    vector.push([3, 5]);
    vector.push([12, 15]);

    println!("original vector {:?}", vector);
    inset_range([0, 0], vector);
    println!("after inserting [0, 0], the vector is now {:?}", vector);

    println!("original vector {:?}", vector);
    inset_range([20, 22], vector);
    println!("after inserting [20, 22], the vector is now {:?}", vector);

    println!("original vector {:?}", vector);
    inset_range([7, 9], vector);
    println!("after inserting [7, 9], the vector is now {:?}", vector);

    println!("original vector {:?}", vector);
    inset_range([10, 11], vector);
    println!("after inserting [10, 11] the vector is now {:?}", vector);

    println!("original vector {:?}", vector);
    inset_range([6, 8], vector);
    println!("after inserting [6, 8] the vector is now {:?}", vector);

    vector.clear();
    vector.push([1, 2]);
    vector.push([3, 5]);
    vector.push([12, 15]);

    println!("original vector {:?}", vector);
    inset_range([2, 4], vector);
    println!("after inserting [2, 4] the vector is now {:?}", vector);
}


// Links
// https://riptutorial.com/rust/example/26442/vectors
// https://doc.rust-lang.org/rust-by-example/primitives/array.html
// https://doc.rust-lang.org/beta/std/vec/struct.Vec.html
// https://doc.rust-lang.org/rust-by-example/std/vec.html
// https://doc.rust-lang.org/std/vec/struct.Vec.html
// https://www.koderhq.com/tutorial/rust/vector/