cmake_minimum_required(VERSION 3.21)
project(PROIECT_SD)

set(CMAKE_CXX_STANDARD 14)

add_executable(PROIECT_SD main.cpp Domain/Set.cpp Domain/Set.h Domain/Node.h Domain/Tree.h Repository/RepositoryFriendship.h Service/ServiceFriendship.cpp Service/ServiceFriendship.h Domain/Friendship.cpp Domain/Friendship.h Domain/Message.cpp Domain/Message.h Repository/RepositoryMessage.h Service/ServiceMessage.cpp Service/ServiceMessage.h)
