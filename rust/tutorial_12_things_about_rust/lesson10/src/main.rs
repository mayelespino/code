

fn main() {
    println!("Lesson10 - functions");
    let x = five();
    println!("x: {}", x);

    let x = plus_one(five());
    println!("x: {}", x);
    println!("is odd: {}", is_odd(five()));
    println!("factorial(10): {}", factorial(10));
}

fn five() ->i32 {
    5
}

fn plus_one(x: i32) -> i32 {
    x + 1
}

fn is_odd(x: i32) -> bool {
    if(x & 1) == 0 {
        false
    } else {
        true
    }
}

fn factorial(x: u64) -> u64 {
    match x {
        0 => 1,
        1 => 1,
        _ => factorial(x - 1) * x,
    }
}