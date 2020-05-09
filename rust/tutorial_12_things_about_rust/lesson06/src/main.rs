fn main() {
    println!("Lesson06 - Strings");
    // str - static string literal
    let howdy = "Howdy√";
    println!("len: {} isEmpty {}", howdy.len(), howdy.is_empty());
    println!("Howdy bytes: {:?}", howdy.as_bytes());
    // strings
    let mut hello = String::from("Hello");
    hello.push('w');
    hello.push_str("orld!");
    println!("String: {}", hello);
    hello.insert(5, ',');
    println!("String: {}", hello);
}
