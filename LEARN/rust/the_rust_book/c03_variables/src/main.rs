fn main() {
    // Variables
    println!("Chapter 3: Programming concepts.");

    let mut x = 5;
    println!("The value of x is: {}", x);
    x = 6;
    println!("The value of x is: {}", x);

    const SUBSCRIBER_COUNT: u32 = 100_000;
    println!("The value of SUBSCRIBER_COUNT is: {}", SUBSCRIBER_COUNT);

    let x = 5;
    println!("The value of x is: {}", x);
    let x = "five";
    println!("The value of x is: {}", x);

    // Scaler and compounded data types.
    let a = 92_222; // Decimal
    let b = 0xFF;   // Hex
    let c = 0o77;   // Octal
    let d = 0b1111_0000; // Binary
    let e = b'A';  // Byte (u8 only)

    // overflow
    let f: u8 = 255;
    // let f: u8 = 256; <- Error
    // in production(?) rust will perform two's complement wrapping, 256 -> 0

   // Floating-point numbers
   let f = 2.0;
   let g: f32 = 3.0;

   // Maths 
   let sum = 5 + 10;
   let difference = 95.0 - 4.3;
   let product = 4 * 30;
   let quotient = 56.7 / 32.2;
   let remainder = 43 % 5;

   // Booleans
    let t = true;
    let f = false;
   
   // Char
   let c = 'a';

    // Compound types
    let tup = ("Let's get rusty!", 100_000);
    let (channel, sub_count) = tup;
    let sub_count = tup.1;

    let error_codes = [200, 404, 500];
    let byte = [0; 8]; // creates [0,0,0,0,0,0,0]

    // functions
    let sum = my_function(11, 22);
    println!("The sum is {}", sum);

    // Control Flow
    let number = 5;

    if number < 10 {
        println!("first condition was true");
    } else if number < 22 {
        println!("second condition was true");
    } else {
        println!("condition was false");
    }

    let condition = true;
    let number = if condition {5} else {6};
    println!("The value of number is {}", number);

    let mut counter = 0;
    let result  = loop {
        counter += 1;

        if counter == 10 {
            break counter;
        }
    };
    println!("The result is {}", result);

    let mut number = 3;

    while number != 0 {
        println!("{}", number);
        number -= 1;
    }

    let a = [ 10, 20, 30, 40, 50 ];
    for element in a.iter() {
        println!("The value is {}", element);
    }

    for number in 1..4 {
        println!("{}!", number);
    }

} // main()

fn my_function(x: i32, y:i32) -> i32 {
    println!("The value of x is: {}", x);
    println!("The value of y is: {}", y);
    x+ y
}

