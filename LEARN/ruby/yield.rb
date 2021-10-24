#!/usr/bin/ruby

def hello
    yield
end

hello {puts "Hello world" }
