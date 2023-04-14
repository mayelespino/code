/*
* Rust tutorial, chapter 13 Testing: https://my.americanhondafinance.com/s/dashboard
* You run the test using "cargo test"
*
*/
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

pub fn greeting(name: &str) -> String { 
    format!("Hello {}!", name)
}

#[cfg(test)]
mod tests {
    
    /*
    #[test]
    fn it_works() {
        let result = 2 + 2;
        assert_eq!(result, 4);
    }

    #[test]
    fn it_panics() {
        panic!("Make this test fail");
    }
    */

    use super::*;
    #[test]
    fn larger_can_hold_smaller() {
        let larger = Rectangle {
            width: 8,
            height: 7,
        };

        let smaller = Rectangle {
            width: 5,
            height: 1,
        };

        assert!(larger.can_hold(&smaller));
    }

    #[test]
    fn smaller_cannot_hold_larger() {
        let larger = Rectangle {
            width: 8,
            height: 7,
        };

        let smaller = Rectangle {
            width: 5,
            height: 1,
        };

        assert!(!smaller.can_hold(&larger));
    }
    /*
    * check out all the assert macros, for example :
    * assert_eq!
    * assert_ne!
    */

    #[test]
    fn test_greeting() {
        let result = greeting("Carol");
        assert!(result.contains("Carol"));
    }

    #[test]
    fn greeting_contains() {
        let result = greeting("Carol");
        assert!(result.contains("Carol"),
        "Greeting did not contain name `{}`",
        result
        );
    }

    #[test]
    // #[should_panic]
    #[should_panic(expect = "panic!")]
    fn panic_on_purpose() {
        panic!("panic!");
    }

    #[test]
    fn it_works() -> Result<(), String> {
        if 2 + 2 == 4 {
            Ok(())
        } else {
            Err(String::from("two plust two does not equal four"))
        }
     }
}
