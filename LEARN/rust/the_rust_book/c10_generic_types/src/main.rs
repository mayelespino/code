/*
* Rust tutorial: https://youtu.be/6rcTSxPJ6Bw
*  
*/

struct Point<T> {
    x: T,
    y: T,
}

impl<T> Point<T> {
    fn x(&self) ->&T {
        &self.x
    }

    fn y(&self) ->&T {
        &self.y
    }
}
/*
* You can have multiple implementation blocks, one for each type or combination.
impl Point<f64> {
    fn x(&self) ->f64 {
        &self.x
    }

    fn y(&self) ->f64 {
        &self.y
    }
}
*/

fn main() {
    println!("Chapter 10 - Generic Types in Rust.");

    // Generics
    let number_list = vec![34, 50, 25, 100, 65];

    let mut largest = number_list[0];

    for number in number_list {
        if number > largest {
            largest = number;
        }
    }

    println!("The largest number is {}", largest);

    //
    let number_list = vec![102, 34, 6000, 89, 54, 2, 43, 8];
    let mut biggest = get_largest(number_list);
    println!("The biggest is: {}", biggest);
    
    //
    let char_list = vec!['y', 'm', 'a', 'q'];
    let mut big = get_largest(char_list);
    println!("big is: {}", big);

    //
    /*
    * moved to top of main
    struct Point<T> {
        x: T,
        y: T,
    }
    */

    let p1 = Point{x:5, y:10};
    let p2 = Point{x:7.0, y:11.0};
    println!("p1 x {} y {}", p1.x(), p1.y());
    println!("p2 x {} y {}", p2.x(), p2.y());

    /*
    * This is how multiple types can be used in enums:
    enum Option<T> {
        Some(T),
        None,
    }

    enum Result<T, E> {
        Ok(T),
        Err(E),
    }
    */

    // The tutorial also shows how to mix and match generic types in an example called mixup.
    // I did not added it here because it just confuses things.
    // The author also goes in to how Rust turns generics in to concrete implementations so
    // there is no performance hit.

}

//
/*
* Now we turn this in to a generic fn
fn get_largest(list: Vec<i32>) -> i32 {
    let mut largest = list[0];

    for item in list {
        if item > largest {
            largest = item;
        }
    }
    largest
}
*/

fn get_largest<T: PartialOrd + Copy>(list: Vec<T>) -> T {
    let mut largest = list[0];

    for item in list {
        if item > largest {
            largest = item;
        }
    }
    largest
}

