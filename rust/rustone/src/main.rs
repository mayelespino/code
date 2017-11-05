use std::thread;

fn main() {
    thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {} from the spawned thread!", i);
        }
    });

    thread::spawn(|| {
        for i in 10..20 {
            println!("hi number {} from the spawned thread!", i);
        }
    });

    for i in 30..35 {
        println!("hi number {} from the main thread!", i);
    }
}