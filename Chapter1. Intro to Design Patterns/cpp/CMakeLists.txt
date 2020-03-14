cmake_minimum_required(VERSION 3.15)
project(cpp)

set(CMAKE_CXX_STANDARD 14)

add_executable(cpp ActionGame.cpp Character.cpp Character.h WeaponBehavior.cpp WeaponBehavior.h)