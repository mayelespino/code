//
// Credit: I typed the code that I got from "Two trie implementations in Rust (one's super fast)" article
// writen by: Tim McNamara and linked bellow.
// I do this the first time then I implement my own.
//

use std::collections::HashMap;

#[derive(Default, Debug)]
struct TrieNode {
    is_end: bool,
    children: HashMap<char, TrieNode>,
} // TrieNode

#[derive(Default, Debug)]
pub struct Trie {
    root: TrieNode,
} // Trie

impl Trie {
    pub fn new() -> Self {
        Trie {
            root: TrieNode::default(),
        }
    } // new()

    pub fn insert(&mut self, word: &str) {
        let mut current_node = &mut self.root;

        for c in word.chars() {
            current_node = current_node.children.entry(c).or_default();
        }
        current_node.is_end = true
    } // insert()

    pub fn contains(&mut self, word: &str) -> bool {
        let mut current_node = &self.root;

        for c in word.chars() {
            match current_node.children.get(&c) {
                Some(node) => current_node = node,
                None => return false,
            }
        }
        current_node.is_end
    } // contains()
} // Trie




fn main() {
    let mut trie = Trie::new();
    trie.insert("hello");
    trie.insert("hi");
    trie.insert("hey");
    trie.insert("world");
    println!("{trie:#?}");
    println!("hiiiii? {}", trie.contains("hiiiii"));
    println!("hi? {}", trie.contains("hi"));
    println!("HI? {}", trie.contains("HI"));
    println!("hello? {}", trie.contains("hello"));
    println!("world? {}", trie.contains("world"));
}

// Links:
// - https://dev.to/timclicks/two-trie-implementations-in-rust-ones-super-fast-2f3m
