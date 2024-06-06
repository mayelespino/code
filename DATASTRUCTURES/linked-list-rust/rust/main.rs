
#[derive(Clone)]
enum address {
    address(Box<my_list>),
    Nil,
}

#[derive(Clone)]
struct my_list {
    value: u32,
    next: address,
}

impl my_list {
    fn append(&mut self, elem: u32) {
        match self.next {
            address::address(ref mut next_address) => {
                next_address.append(elem);
            }
            address::Nil => {
                let node = my_list {
                    value: elem,
                    next: address::Nil,
                };
                self.next = address::address(Box::new(node))
            }
        }
    }

//    fn delete(&mut self, elem: u32) {
//        match self.next {
//            address::address(ref mut next_address) => {
//                if next_address.value == elem {
//                    println!("Deleting value {}", next_address.value);
//                    self.next = next_address.next.clone();
//                } else {
//                    next_address.delete(elem);
//                }
//            }
//            address::Nil => {
//                if self.value == elem {
//                    self.value = 0;
//                } else {
//                    println!("Element {} does not exist in the linked list", elem);
//                }
//            }
//        }
//    }

    fn count(&self) -> u32 {
        match self.next {
        address::address(ref newaddress) => 1 + newaddress.count(),
        address::Nil => 0,
        }
    }

    fn list(&self) {
        if self.value == 0 {
            println!("The list is empty")
        } else {
            println!("{}", self.value);
            match self.next {
                address::address(ref next_address) => next_address.list(),
                address::Nil => {}
            }
        }
    }

//    fn update(&mut self, index: u32, elem: u32) {
//        let mut i = 0;
//        let mut j = self;
//        if i == index {
//            j.value = elem;
//        }
//        while i < index {
//            // println!("{}", j.value);
//            match j.next {
//                address::address(ref mut next_address) => j = next_address,
//                address::Nil => {}
//            }
//            i = i + 1;
//        }
//        j.value = elem;
//    }

}


fn main() {
    let mut head = my_list {
        value: 8,
        next: address::Nil,
    };
    head.append(9);
    head.append(10);
    head.append(11);
    head.list();
    println!("The size of the list is {}", head.count());
//    head.update(4, 20);
//    head.update(0, 6);
    head.list();
}


// https://stackoverflow.com/questions/41653148/singly-linked-list-in-rust