/*
* From the rust tutorial: https://youtu.be/n3bPhdiJm9I 
*/

struct User {
    username: String,
    email: String,
    active: bool,
    sign_in_count: u32,
}

#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

// These are methods, they pass &self
impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }

    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}

// These are associated methods, they do not pass &self
impl Rectangle {
    fn square(size: u32) -> Rectangle {
        Rectangle {
            width: size,
            height: size
        }
    }
}

fn main() {
    println!("Chapter 05  structs");

    let mut user1 = User {
            email: String::from("me@me.me"),
            username: String::from("me"),
            active: true,
            sign_in_count: 1
            };

    let name = user1.username;
    user1.username = String::from("wallace123");

    let user2 = build_user(String::from("john"), String::from("john@thebeathels.com"));

    let user3 = User {
        username: String::from("john"),
        email: String::from("john@ledzeppelin.com"),
        ..user2
    };


    // Tuple structs
    struct Color(i32, i32, i32);
    struct Point(i32, i32, i32);

    let rect = Rectangle {
        width: 30,
        height: 50
    };

    let rect1 = Rectangle {
        width: 20,
        height: 40
    };

    let rect2 = Rectangle {
        width: 40,
        height: 50
    };

    let rect3 = Rectangle::square(25);

    println!("Can rect hold rect1? {}", rect.can_hold(&rect1));
    println!("Can rect hold rect2? {}", rect.can_hold(&rect2));

    println!("{:#?}", rect);
    println!("The area of the rectangle is {}", rect.area());


} // main()

fn build_user(email: String, username: String) -> User {
    User {
        email, // the short form is to just have: email, instead of email: email,
        username,
        active: true,
        sign_in_count: 1,
        }
}

/*
* Deleted in favor or a method function
fn area(rectangle: &Rectangle) -> u32 {
    rectangle.width * rectangle.height
}
*/

//EOF
