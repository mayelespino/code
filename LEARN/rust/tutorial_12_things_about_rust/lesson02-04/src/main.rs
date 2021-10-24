#![allow(unused_variables)]

fn main() {
    println!("Leson02 - mut");
    // mut
    let mut x = 0;
    println!("x is mutable, val = {}", x);
    x = 100;
    println!("x is mutable, val = {}",x);

    println!("Leson03 - shadow ");
    // shadow
    let y = 5;
    let y = y + 1;
    let  y = y * 2;
    eprintln!("y (shadow) value is: {}", y);
    // shadow and change type
    let abc = "ABC";
    let abc = abc.len();
    println!("abc is: {} ", abc);

    println!("Leson04 - consts");
    const FHD_WIDTH: u32 = 1920;
    const BAD_PI: f32 = 22.0/7.0;
    println!("FHD_WIDTH is {}, BAD_PI is {}", FHD_WIDTH, BAD_PI)
}
