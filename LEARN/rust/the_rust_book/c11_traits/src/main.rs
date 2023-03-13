/*
* rust tutorial link: https://youtu.be/T0Xfltu4h3A
*/

pub struct NewsArticle {
    pub author: String,
    pub headline: String,
    pub content: String,
}

impl Summary for NewsArticle {
    fn summarize(&self) -> String {
        format!("{} by {}", self.headline, self.author)
    }
}

pub struct Tweet {
    pub username: String,
    pub content: String,
    pub reply: bool,
    pub retweet: bool,
}

impl Summary for Tweet {
    fn summarize(&self) -> String {
        format!("{} : {}", self.username, self.content)
    }
}

/*
* Example of a default implementation
pub trait Summary {
    fn summarize(&self) -> String {
        String::from("Read more....")
    }
}
*/

pub fn notify(item: &impl Summary) {
    println!("Breaking news! {}", item.summarize());
}

pub trait Summary {
    fn summarize(&self) -> String;
}

/*
* The above is syntax sugar for:
pub fn notify<T: Summary>(item: &T) {
    println!("Breaking news! {}", item.summarize());
}

a more complex example:
pub fn notify<T: Summary>(item1:&T, item2: &T) {
    .....
}

another example:
pub fn some_function<T, U>(t: &T, u: &U) ->i32 {
    where   T: Display + Clone,
            U: Clone + Debut
    .....
}

using as return type:
pub fn returns_summarizable() -> impl Summary {
    Tweet {
        username ...,
        content ....,
        ....
    } // no ; because this is the return.
}

The tutorial also touched on chained traits and how you can have multiple (differntly defined) traits for an implementation.
*/

fn main() {
    println!("Chapter 11 - Traits");

    let article = NewsArticle {
        author: String::from("John Doe"),
        headline: String::from("The sky if falling."),
        content: String::from("The sky if falling.")
    };

    let tweet = Tweet {
        username: String::from("@johndoe"),
        content: String::from("Hello world!"),
        reply: false,
        retweet: false
    };

    println!("Tweet summary: {}", tweet.summarize());
    println!("Article summary: {}", article.summarize());
   
    notify(&article);
    notify(&tweet);
}
