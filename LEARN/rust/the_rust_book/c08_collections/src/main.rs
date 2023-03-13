/*
* Rust tutorial: 
* Common Collections
*/

use unicode_segmentation::UnicodeSegmentation;
use std::collections::HashMap;

fn main() {
    println!("Chapter 8 - Common collections");

    let a = [1, 2, 3];
    let mut v:Vec<i32> = Vec::new();
    v.push(1);
    v.push(2);
    v.push(3);

    {
        let v2 = vec![1, 2, 3];
    } // v2 and all it's elements are dropped.

    let mut v = vec![1, 2, 3, 4, 5];
    let third = &v[2]; // With this approach you can specify an invalid index and get a runtime error, &v[20]
    println!("The third element is {}", third);

    match v.get(2) {
        Some(third) => println!("The third element is {}", third),
        None => println!("There is no element at that index.")
    }

    for i in &v {
        println!("{}", i); 
    }


    for i in &mut v {
        *i += 50;
        println!("{}", i); 
    }

    enum SpreadsheetCell {
        Int(i32),
        Float(f64),
        Text(String),
    }

    let row = vec![
        SpreadsheetCell::Int(3),
        SpreadsheetCell::Text(String::from("blue")),
        SpreadsheetCell::Float(10.12),
    ];

    match &row[1] {
        SpreadsheetCell::Int(i) => println!("{}", i),
        _ => println!("Not an integer!")
    };

    match &row[0] {
        SpreadsheetCell::Int(i) => println!("{}", i),
        _ => println!("Not an integer!")
    };

    let mut s = String::from("foo");
    s.push_str("bar");
    s.push('!');
    println!("s = {}", s);

    let s1 =String::from("Hello, ");
    let s2 = String::from("world!");
    let s3 = s1 + &s2;
    println!("s3 = {}", s3);

    let s4 =String::from("Hello, ");
    let s5 = String::from("world!");
    let s6 = format!("{}{}", s4, s5);
    println!("s6 = {}", s6);

    for b in "#$%*()_".bytes() {
        println!("{}", b);
    }

    for c in "#$%*()_".chars() {
        println!("{}", c);
    }


    for g in "#$%*()_".graphemes(true) {
        println!("{}", g);
    }
    
    let blue =  String::from("Blue");
    let yellow = String::from("Yellow");

    let mut scores = HashMap::new();

    scores.insert(blue, 10);
    scores.insert(yellow, 50);
    let team_name = String::from("Blue");
    let score = scores.get(&team_name); // we can not use get(&blue) because ownership was transfered.
    
    for (key, value) in &scores {
        println!("{} {}", key, value);
    }
    
    scores.insert(String::from("Blue"), 10);
    scores.insert(String::from("Blue"), 20);

    scores.entry(String::from("Yellow")).or_insert(30);
    scores.entry(String::from("Yellow")).or_insert(40);

    let text = "hello world wonderful world";

    let mut map = HashMap::new();

    for word in text.split_whitespace() {
        let count = map.entry(word).or_insert(0);
        *count += 1;
    }
    println!("{:?}", map);
}
