
fn recursive_fibonacci(val: i64) -> i64 {
    if val < 2{
        val
    } else {
        (recursive_fibonacci(val-1) + recursive_fibonacci(val-2))
    }
}

fn main() {
    println!("Recursive Fibonacci");
    println!("Fib(10)");
    let mut result = recursive_fibonacci(10);
    println!("Result of 10: {}", result);
//    println!("Fib(100)");
//    result = recursive_fibonacci(100);
//    println!("Result of 100: {}", result);

}
