#![allow(unused_parens)]

fn main() {
    println!("Lesson09 - Expressions and statements");
    let a = 3 + 7;
    let b = (3 + 7);
    let c = {3 + 7};
    println!("a: {} b: {} c: {}", a, b, c);
    let y = {
        let mut x = 3;
        x = x * 2;
        x + 1
        // there is no ;  as it is an expression.
    };
    println!("y: {}", y);
}
