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

Node<char>* at(unsigned int i, Node<char>* head) {
	while (head != nullptr && i--) head = head->next;
	return head;
}

void delete_node(Node<char>* node) {
	// NOTE: node is neither the first nor the last in the list
	Node<char> *next = node->next;
	node->data = next->data;
	node->next = next->next;
	delete next;
}


TEST_CASE( "Deletes middle node" ) {
	// Remove single
	Node<char>* list = make_list('a', 'b', 'c', 'd', 'e', 'f');
	Node<char>* node = at(2, list);
	REQUIRE( node->data == 'c' );
	delete_node(node);
	Node<char>* target = make_list('a', 'b', 'd', 'e', 'f');
	REQUIRE( listequal(list, target) );
	delete_list(list);
	delete_list(target);

	// Remove muiltiple
	list = make_list('a', 'b', 'c', 'd', 'e', 'f');
	node = at(1, list);
	REQUIRE( node->data == 'b' );
	delete_node(node);
	node = at(3, list);
	REQUIRE( node->data == 'e' );
	delete_node(node);
	node = at(2, list);
	REQUIRE( node->data == 'd' );
	delete_node(node);
	target = make_list('a', 'c', 'f');
	REQUIRE( listequal(list, target) );
	delete_list(list);
	delete_list(target);
}
