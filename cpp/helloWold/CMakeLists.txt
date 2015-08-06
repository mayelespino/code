cmake_minimum_required(VERSION 2.8.4)
project(helloWold)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES main.cpp)
add_executable(helloWold ${SOURCE_FILES})