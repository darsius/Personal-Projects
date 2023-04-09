#pragma once

template <typename T> class Tree;
template <class T>
class Node{
private:
    T info;
    Node<T>* left;
    Node<T>* right;
public:
    Node(T info) {
        this->left = nullptr;
        this->right = nullptr;
        this->info = info;
    }
    ///constructorul va initializa datele membru

    Node (T info, Node<T>* left, Node<T>* right) {
        this->left = left;
        this->right = right;
        this->info = info;
    };
    ///constructorul de atribuire

    friend class Tree<T>;
};