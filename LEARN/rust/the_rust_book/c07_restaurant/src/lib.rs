/*
* Lets get rusty tutorial: https://youtu.be/5RPXgDQrjio
* This folder is the library crate for c07_module_system
* This following test was added automatically, we do not use it yet.
#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        let result = 2 + 2;
        assert_eq!(result, 4);
    }
}
*/

pub use crate::front_of_house::hosting;
// use self::front_of_house::hosting;

use rand::{Rng, CryptoRng, ErrorKind::Transient};
use std::io::{self, Write};
// This is how you import all public items in a module:
// use std::io::*;

/*
* Now we move front of house to it's own file
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}

        pub fn seat_at_table() {}
    }

    pub mod serving {
        pub fn take_order() {}

        pub fn serve_order() {}

        pub fn take_payment() {}
    }
}
then this is how we reference after the move:
*/
mod front_of_house;

mod back_of_house {
    
    pub struct Breakfast {
        toast: String,
        seasonal_fruit: String,
    }

    pub enum Appetizer {
        Soup,
        Salad,
    }

    impl Breakfast {
        pub fin summer(toast: &str) -> Breakfast {
            Breakfast {
                pub toast: String::from(toast),
                pub seasonal_fruit: String::from("peaches");
            }
        }
    }

    pub fn fix_incorrect_order() {
        cook_order();
        super::serve_order();
    }

    pub fn cook_order() {}
}


pub fn eat_at_restaurant() {
    // Absolute path
    // crate::front_of_house::hosting::add_to_waitlist();

    // Relative path
    // front_of_house::hosting::add_to_waitlist();
    // since we now have the USE directive
    hosting::add_to_waitlist();
    

    let mut meal: Breakfast = back_of_house::Breakfast::summer("Rye");
    meal.toast = String::from("Wheat");

    let order1 = back_of_house::Appetizer::Soup;
    let order2 = back_of_house::Appetizer::Salad;

    let secret_number = rand::thread_rng().gen_range(1, 101);
};
