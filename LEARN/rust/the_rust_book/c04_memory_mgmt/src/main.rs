/*
* From tutorial "lets get rusty" : https://youtu.be/VFIOSWy93H0
*/
fn main() {
    println!("Chapter 4 - Memory Management.");

    fn a() {
        let x = "hello"; // Created in Stack.
        let y = 22;
    }
    
    fn b() {
        let x = String::from("world"); // Created on Heap
    }

    /*
    * --- Ownership rules ---
    * 1. Each value in Rust has a variable that's called its owner.
    * 2. There can be only one owner at a time.
    * 3. When the owner goes out of scope, the value is dropped.
    */
    let x = 5;
    let y = x; // Copy the value (5)

    let s1 = String::from("hello");
    let s2 = s1; // This does a move, so it changes owner.
    // println!("value in s1 {}", s1);
    /*
    26 |     let s2 = s1; // This does a move, so it changes owner.
       |              -- value moved here
    27 |     println!("value in s1 {}", s1);
       |                                ^^ value borrowed here after move
    */
    let s3 = s2.clone();
     println!("value in s3 {}", s3);

    // Call a function that takes ownership
    take_ownership(s3);
    /*
    println!("{}", s3);
    38 |     take_ownership(s3);
       |                    -- value moved here
    39 |     println!("{}", s3);
       |                    ^^ value borrowed here after move
    */    

    let x = 5;
    makes_copy(x);
    println!("{}", x);

    let s4 = gives_ownership();
    println!("s4 : {} ", s4);

    let s5 = takes_and_gives_back(s4);
    // println!("s4 : {} ", s4); This gets a borrow error
    println!("s5 : {} ", s5);

    let len = calculate_length(&s5);
    println!("len: {}", len);

    // You can only have 1 mutable reference to data in a scope.
    // You can NOT have a mutable reference if a unmutable reference already exists.
    let mut s6 = String::from("Hello ");
    change(&mut s6);
    println!("s6: {}", s6);

    // once the rabialbe goes out os scope, you can have another mutable reference.
    let mut s7 = String::from("hey");
    let r1 = &s7;
    let r2 = &s7;
    println!("{} {}", r1, r2); // Here r1 and r2 go out of scope.
    let r3 = &mut s7;
    println!("s7: {}", s7);

    // Rules of references:
    // 1. At any given time, you can have either one mutable referemce or
    // any number of immutable references.
    //
    // 2. References must always be valid.

    // Slices follow the same rules as references.
    let hello = &s6[0..6];
    println!("{}", hello);


} // main()


/*
*
*/
fn take_ownership(some_string: String) {
    println!("{}", some_string);
}

/*
* This function make a copy automatically, because this is an integer, and is in the stack.
*/
fn makes_copy(some_integer: i32) {
    println!("{}", some_integer);
}

fn gives_ownership() -> String {
    let some_string = String::from("yo!");
    some_string
}

fn takes_and_gives_back(a_string: String) -> String {
    a_string
}

fn calculate_length(s: &String) -> usize {
    let length = s.len();
    length
}

fn change(some_string: &mut String) {
    some_string.push_str(", world!");
}



// EOF
