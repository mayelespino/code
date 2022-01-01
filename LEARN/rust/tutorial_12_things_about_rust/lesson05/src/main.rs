fn main() {
    println!("Lesson05 - Basic Types");
    let x128: usize = 0xAAAAAAAA_AAAAAAAA_AAAAAAAA_AAAAAAAA;
    let x64: i64 = 123456;
    // 32 bit, 64 bit floating point numbers
    let x = 2.0; //f64
    let y: f32 = 3.0; //f32
    println!("x128 {}, x64 {}, x {}, y {}", x128, x64, x, y);
    // Chars
    let c = 'c';
    let z = 'Z';
    let done = false;
    println!("Some chars: {} {} {}", c, z, done);
}
