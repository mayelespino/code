cmake_minimum_required(VERSION 3.6)
project(cpp)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES
    helloWold/hello.cpp
    helloWold/main.cpp
    reverseAString/main.cpp
    traverseTree/main.cpp
    traverseTree/traverseTree.cpp
    traverseTree2/main.cpp)

add_executable(cpp ${SOURCE_FILES})