use std::error::Error;
use std::fs::File;
use std::io::prelude::*;
use std::env;


fn search_case_insensitive<'a>(query: &str, contents: &'a str) -> Vec<&'a str> {
    let query = query.to_lowercase();
    let mut results = Vec::new();

    for line in contents.lines() {
        if line.to_lowercase().contains(&query) {
            results.push(line);
        }
    }

    results
}

pub fn search<'a>(query: &str, contents: &'a str) -> Vec<&'a str> {
        let mut results = Vec::new();

        for line in contents.lines() {
         if line.contains(query) {
                results.push(line);
                }
        }
        results
}

pub fn run(config: Config) -> Result<(), Box<Error>>{
        let mut f = File::open(config.filename)?;

        let mut contents = String::new();
        f.read_to_string(&mut contents)?;

         let results = if config.case_sensitive {
                search(&config.query, &contents)
        } else {
                search_case_insensitive(&config.query, &contents)
        };

        println!("---------------------------");
        for line in results {
                println!("{}", line);
        }
        println!("---------------------------");

        Ok(())
}

pub struct Config {
    pub query: String,
    pub filename: String,
    pub case_sensitive: bool,
}

impl Config {
    pub fn new(args: &[String]) -> Result<Config, &'static str> {
        if args.len() < 3 {
            return Err("not enough arguments");
        }

        let query = args[1].clone();
        let filename = args[2].clone();
        let case_sensitive = env::var("CASE_INSENSITIVE").is_err();

        Ok(Config { query, filename, case_sensitive })
    }
}


#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn one_result() {
        let query = "duct";
        let contents = "\
Rust:
fast, safe, productive.
Pick three.  
Duct tape.";
    assert_eq!(
        vec!["fast, safe, productive."],
        search(query, contents)
    )
    }

    #[test]
    fn case_insensitive() {
        let query = "rUsT";
        let contents = "\
Rust:
safe, fast, productive.
Pick three.
Trust me.";

        assert_eq!(
            vec!["Rust:", "Trust me."],
            search_case_insensitive(query, contents)
        );
    }

}

