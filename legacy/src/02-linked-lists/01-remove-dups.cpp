#include <unordered_set>
#include <vector>
#include <array>
#include <cstdarg>
#include <iostream>
#include <concepts>
#include <catch2/catch_test_macros.hpp>


// begin linked list node definition
template<typename T>
concept Streamable = 
	requires(std::ostream &os, T value) {
		{ os << value } -> std::convertible_to<std::ostream &>;
	};

template<typename T>
concept NodeData = std::equality_comparable<T> && std::default_initializable<T> && Streamable<T>;

template<NodeData T>
struct Node {
	T data;
	Node *next;

	Node() : data(), next(nullptr) {}
	Node(const T& new_data) : data(new_data), next(nullptr) {}

};


template<NodeData T>
std::ostream& operator<<(std::ostream& os, const Node<T>* node) {
	const Node<T> *p = node;
	os << p -> data;
	while ((p = p -> next) != nullptr) {
		os << " -> " << p -> data;
	}
	return os;
}


template<NodeData T>
bool listequal(const Node<T>* head1, const Node<T>* head2) {
	while (head1 != nullptr && head2 != nullptr) {
		if (head1->data != head2->data)
			return false;

		head1 = head1->next;
		head2 = head2->next;
	}
	if (head1 || head2) return false;
	return true;
}


template<NodeData T>
Node<T>* make_list() {
    return nullptr;
}

template<NodeData T, typename... Args>
Node<T>* make_list(const T& value, const Args&... args) {
    Node<T>* head = new Node<T>(value);
    head->next = make_list<T>(args...);
    return head;
}


template<NodeData T>
void delete_list(Node<T>* head) {
	Node<T> *current = head;
	while (current != nullptr) {
		Node<T> *next = current -> next;
		delete current;
		current = next;
	}
}
// end linked list node definition

void remove_duplicates(Node<int>* head) {
	if (head == nullptr) return;

	std::unordered_set<int> seen{head->data};
	Node<int>* prev = head;
	Node<int>* current = head->next;

	while (current != nullptr) {
		if (seen.contains(current->data)) {
			Node<int>* tmp = current;
			prev->next = current->next;
			current = tmp->next;
			delete tmp;
		} else {
			seen.insert(current->data);
			prev = current;
			current = current->next;
		}
	}
}

TEST_CASE( "Removes duplicates" ) {
	Node<int>* list = make_list(1, 2, 3, 4, 5);
	Node<int>* dedup  = make_list(1, 2, 3, 4, 5);
	remove_duplicates(list);
	REQUIRE( listequal(list, dedup) );
	delete_list(list);
	delete_list(dedup);


	list = make_list(1, 1, 2, 3, 4, 5, 3, 4, 1);
	dedup  = make_list(1, 2, 3, 4, 5);
	remove_duplicates(list);
	REQUIRE( listequal(list, dedup) );
	delete_list(list);
	delete_list(dedup);

	list = make_list(4, 3, 6, 6, 3, 12, -1, 3, 12, 12, 12, -2, 3);
	dedup  = make_list(4, 3, 6, 12, -1, -2);
	remove_duplicates(list);
	REQUIRE( listequal(list, dedup) );
	delete_list(list);
	delete_list(dedup);
}
