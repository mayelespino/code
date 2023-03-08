/*
* The rust tutorial: https://youtu.be/wM6o70NAWUI
*
*/

use std::fs::{self,File};
use std::io;
use std::io::Read;

fn main() {
    println!("C09 - Errors");

    //panic!("crash and burn"); //is used to exit immediatly, unrecoverable error.
    // use this with RUST_BACKTRACE=1

    /*
    let f = File::open("hello.txt");

    let f = match f {
        Ok(file) => file,
        Err(error) => panic!("Problem opening the file {:?}", error),
    };
    */

    let f = File::open("hello.txt").expect("Failed to open hello.txt");
    let name = read_username_from_file();
    match name {
        Ok(s) => println!("name is: {}", s),
        Err(err) => println!("{}", err),
    };
}


fn read_username_from_file() -> Result<String, io::Error> {

    // let mut f = File::open("hello.txt")?;

    // all this can be ommited by adding the "?" to the call above
    // let mut f = match f {
    //     Ok(file) => file,
    //     Err(e) => return Err(e),
    //  };
    
    // let mut s = String::new();

    /*
    * Same here, if we add "?", the following is simplified
    match f.read_to_string(&mut s) {
        Ok(_) => Ok(s),
        Err(e) => Err(e),
    };
    
    as followes:
    f.read_to_string(&mut s)?;
    Ok(s)
    */

    // even simpler:
    // File::open("hello.txt")?.read_to_string(&mut s)?;
    // Ok(s)

    // Now we use a convienence function in fs that does all of this:
    fs::read_to_string("hello.txt")
}
