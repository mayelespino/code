
fn main() {
    println!("lesson11_12 - loops");
    let mut counter = 0;
    let result = loop {
        counter += 1;
        if counter == 10 {
            break counter * 2
        }
    };
    println!("result: {} ", result);

    counter = 3;
    while counter != 0 {
        println!("counter: {} ", counter);
        counter -=1 ;
    }


    let a = [10, 20, 30 , 40, 50];
    for element in a.iter() {
        println!("element: {} ", element);
    }

    // using reange, number >= 1 and number < 4
    for number in (1..4).rev() {
        println!("number: {} ", number);
    }
}
