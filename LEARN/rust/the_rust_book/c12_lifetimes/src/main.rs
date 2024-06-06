/*
* Rust tutorial: https://youtu.be/juIINGuZyBc
* Lifetimes
*
*/

struct ImportantExcerpt<'a> {
    part: &'a str,
}

impl<'a> ImportantExcerpt<'a> {
    fn return_part(&self, announcement: &str) -> &str {
        println!("Attention please: {}", announcement);
        self.part
    }
}

fn main() {
    println!("Chapter 12 - lifetimes.");

    /* 
    * The base case, here both lifetimes are the same.
    let string1 = String::from("abc");
    let string2 = String::from("xyz");

    let result = longest(string1.as_str(), string2.as_str());
    println!("The longest string is {}", result);
    */

    // This works because result is received when both livetimes are valid 
    // in scope
    let string1 = String::from("abc");
    {
        let string2 = String::from("xyz");
        let result = longest(string1.as_str(), string2.as_str());
        println!("The longest string is {}", result);
    }

    /*
    * This will not work becase the result is examined when the shortest 
    * lifetime is invalid (out of scope).
    let string1 = String::from("abc");
    {
        let string2 = String::from("xyz");
        let result = longest(string1.as_str(), string2.as_str());
    }
    println!("The longest string is {}", result);
    */

    let novel = String::from("Call me Ishmael. Some years ago...");
    let first_sentence = novel.split('.').expect("Could not find .");
    let i =  ImportantExcerpt {
        part: first_sentence,
    };

    /*
    * 1. Each parameter that is a reference gets its own lifetime parameter.
    * 2. If there is exactly one lifetime parameter, that lifetime is assigned
    *    to alloutput lifetime parameters.
    * 3. If there are multiple input lifetime parameters, but one of them is &self 
    *    or &mut self the lifetime of self is assigned to all output lifetime parameters.
    */

    //Static lifetime, all strings have an implicit static lifetime.
    let s: &'static str = "I jave a static lifetime.";
}

fn longest<'a>(x: & 'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
