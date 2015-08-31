cmake_minimum_required(VERSION 3.2)
project(c)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES
    linked-lists/circular-single-link-list.c
    linked-lists/singly-linked-list.c
    traverseTree/traverseTree.c)

add_executable(c ${SOURCE_FILES} linked-lists/source_file.h linked-lists/source_file.cpp)