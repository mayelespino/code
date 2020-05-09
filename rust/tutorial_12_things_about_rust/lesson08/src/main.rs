fn main() {
    println!("Lesson 08 - Arrays");
    //Arrays must all be the same size
    let a = [1, 2, 3, 4, 5];
    let b: [u16; 5] = [1, 2, 3, 4, 5];
    let c = [0; 5];
    println!("a: {:?} b: {:?} c: {:?}", a, b, c);
    let months = ["Jan","Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
    let first = a[0];
    let nov = months[10];
    println!("first: {} nov: {}", first, nov);
}
