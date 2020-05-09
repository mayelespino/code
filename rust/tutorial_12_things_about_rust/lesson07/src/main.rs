#![allow(unused_variables)]
fn main() {
    println!("Lesson 07 - Tuples");
    // tuples can have different types and fixed lenght
    let tup: (i32, f64, u8, f32) = (500, 6.4, 1, 29.29);
    //
    let tup2 = (1500, 3.4);
    println!("tup {:?} tup2 {:?}", tup, tup2);
    let (w, x, y, z) = tup;
    println!("w:{} x:{} y:{} z:{}", w, x, y, z);
    let a = tup.0;
    let b = tup2.1;
    let c = tup.3;
    println!("a:{} b:{} c:{}",a ,b , c);
}
