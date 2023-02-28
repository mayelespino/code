/*
* Tutorial: https://youtu.be/DSZqIJhkNCM
* Enums and Pattern matching
*/

// enum IpAddrKind {
//     V4,
//     V6
// }

// enum IpAddrKind {
//     V4(String),
//     V6(String),
// }



enum IpAddrKind {
    V4(u8, u8, u8, u8),
    V6(String),
}


struct IpAddr {
    kind: IpAddrKind,
    address: String,
}


enum Message {
    Quit,
    Move {x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}

impl Message {
    fn message() {
        println!("Hello!");
    }
}


#[derive(Debug)]
enum UsState {
    Alabama,
    Alaska,
    Arizona,
    Arkansas,
    California,
    //...
}

enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter(UsState),
}

// fn value_in_cents(coin: Coin) -> u8 {
//     match coin {
//         Coin::Penny => 1,
//         Coin::Nickel = 5,
//         Coin::Dime => 10,
//         Coin::Quarter => 25,
//     }
// }

fn value_in_cents(coin: Coin) -> u8 {
    match coin {
        Coin::Penny => 1,
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter(state) => {
            println!("State quarter from {:?}!", state);
            25
        }
        _ => 0, // Matches every other value (catch all)  
    }
}


fn plus_one(x: Option<i32>) -> Option<i32> {
    match x {
        None => None,
        Some(i) => Some(i+1),
    }
}

fn main() {
    println!("Chapter 06 - Enums and Pattern matching.");

    let four = IpAddrKind::V4;
    let six = IpAddrKind::V6;

    // let localhost = IpAddr {
    //     kind: IpAddrKind::V4,
    //     address: String::from("127.0.0.1")
    // };

    // let localhost = IpAddrKind::V4(String::from("127.0.0.1"));
    let localhost = IpAddrKind::V4(127, 0, 0, 1);

    // enum Option<T> {
    //     Some(T),
    //     None,
    // }

    let some_number = Some(5);
    let some_string = Some("string");
    let absent_number: Option<i32> = None;

    let x: i8 = 5;
    let y: Option<i8> = Some(5); //or = None
    
    // you can not sum an int to an option, so we use the unwrap_or()
    let sum = x + y.unwrap_or(0);

    value_in_cents(Coin::Quarter(UsState::Alaska));

    let five = Some(5);
    let six = plus_one(five);
    let none = plus_one(None);

    // if let Some(3) = some_value { // Read more about this, it is now used much?
    //     println!("three");
    // } 

}
