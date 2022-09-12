use std::thread;

static NTHREADS: i32 = 10;


// This is the `main` thread
fn main() {
    // Make a vector to hold the children which are spawned.
    let mut children = vec![];

    //
    let mut current_floor: [usize; 10] = [1; 10];
    let mut requested_floor: [usize; 10] = [1; 10];

    for i in 0..NTHREADS {
        // Spin up another thread
        children.push(thread::spawn(move || {
            //let mut index : usize = i as usize;
            current_floor[i as usize] = 1;
            requested_floor[i as usize] = i as usize;
            println!("elevator {} - Current floor {} - Requested floor {}", i as usize, current_floor[i as usize], requested_floor[i as usize]);

        }));
    }

    println!("Before joining");
    for child in children {
        // Wait for the thread to finish. Returns a result.
        let _ = child.join();
    }
    println!("After joining");
}
