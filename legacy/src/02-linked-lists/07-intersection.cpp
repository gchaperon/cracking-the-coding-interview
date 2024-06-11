#include <cmath>
#include <unordered_map>
#include <algorithm>
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
	if (node == nullptr) return os;
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
	while (head != nullptr && i-- > 0) head = head->next;
	return head;
}

Node<char>* intersection(Node<char> *h1, Node<char> *h2) {
	Node<char> *index;
	std::unordered_map<Node<char>*, int> lengths = {{h1, 0}, {h2, 0}};

	for (index = h1; index; index=index->next) lengths[h1]++;
	for (index = h2; index; index=index->next) lengths[h2]++;

	int shortl = std::minmax(lengths.at(h1), lengths.at(h2)).first;
	Node<char> *shorth, *longh;
	std::tie(shorth, longh) = std::minmax(
		h1, h2, [lengths](auto p1, auto p2) -> bool {
			return lengths.at(p1) < lengths.at(p2); });

	int difference = std::abs(lengths.at(h1) - lengths.at(h2));
	index = longh;
	for (int i = 0; i < difference; i++) index = index->next;

	// apply intersection checking for same-size lists shorth and index;
	for (int i = 0; i < shortl; shorth=shorth->next, index=index->next, i++)
		if (shorth == index)
			return index;
	return nullptr;
}


TEST_CASE( "Finds intersection" ) {
	Node<char> *l1, *l2, *result, *target;
	// two empty lists don't intersect
	l1 = make_list<char>();
	l2 = make_list<char>();
	result = intersection(l1, l2);
	target = make_list<char>();
	REQUIRE( listequal(result, target) );
	delete_list(l1);
	delete_list(l2);
	delete_list(target);

	// one emtpy and one non-empyt don't intersect
	l1 = make_list<char>();
	l2 = make_list('a', 'b', 'c');
	result = intersection(l1, l2);
	target = make_list<char>();
	REQUIRE( listequal(result, target) );
	std::cout << "t2 good!" << std::endl;
	delete_list(l1);
	delete_list(l2);
	delete_list(target);
	
	// two lists that don't intersect
	l1 = make_list('a', 'b');
	l2 = make_list('a', 'b', 'c', 'd');
	result = intersection(l1, l2);
	target = make_list<char>();
	REQUIRE( listequal(result, target) );
	delete_list(l1);
	delete_list(l2);
	delete_list(target);
	
	// same length, intersect early
	l1 = make_list('a', 'b', 'c', 'd');
	l2 = l1;
	result = intersection(l1, l2);
	target = make_list('a', 'b', 'c', 'd');
	REQUIRE( listequal(result, target) );
	delete_list(l1);
	delete_list(target);
	
	// same length, intersect late
	l1 = make_list('a', 'b', 'c', 'd');
	l2 = make_list('e', 'f', 'g');
	at(2, l2)->next = at(3, l1);
	result = intersection(l1, l2);
	target = make_list('d');
	REQUIRE( listequal(result, target) );
	at(2, l2)->next = nullptr;
	delete_list(l1);
	delete_list(l2);
	delete_list(target);
	
	// different lengths, intersect in middle of short
	l1 = make_list('a', 'b', 'c');
	l2 = make_list('d', 'e', 'f', 'g', 'e', 'h');
	at(5, l2)->next = at(1, l1);
	result = intersection(l1, l2);
	target = make_list('b', 'c');
	REQUIRE( listequal(result, target) );
	at(5, l2)->next = nullptr;
	delete_list(l1);
	delete_list(l2);
	delete_list(target);

	// different lengths, shorter is sublist
	l1 = make_list('a', 'b', 'c', 'd', 'e', 'f', 'g');
	l2 = at(4, l1);
	result = intersection(l1, l2);
	target = make_list('e', 'f', 'g');
	REQUIRE( listequal(result, target) );
	delete_list(l1);
	delete_list(target);

	// different lengths, no intersection
	l1 = make_list('a', 'b', 'c', 'd');
	l2 = make_list('e', 'f');
	result = intersection(l1, l2);
	target = make_list<char>();
	REQUIRE( listequal(result, target) );
	delete_list(l1);
	delete_list(l2);
	delete_list(target);
}
