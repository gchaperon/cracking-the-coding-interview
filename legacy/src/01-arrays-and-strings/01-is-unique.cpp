#include <string_view>
#include <set>
#include <catch2/catch_test_macros.hpp>

bool is_unique( std::string_view s) {
	return std::set<char>(begin(s), end(s)).size() == s.size();
}

bool is_unique_no_data_structure(std::string_view s) {
	bool seen[ 1 << (sizeof(char) * 8) ] = { false };

	for (unsigned char c : s) {
		if (seen[c]) return false;
		seen[c] = true;
	}
	return true;
}

typedef bool (*Fn) ( std::string_view );

TEST_CASE( "All unique" ) {
	Fn impls[] = {is_unique, is_unique_no_data_structure};
	for (auto impl : impls) {
		REQUIRE( impl("") );
		REQUIRE( !impl("aaaa") );
		REQUIRE( impl("abcd") );
		REQUIRE( impl("a jqmp") );
		REQUIRE( !impl("hola que tal") );
		REQUIRE( !impl("abcdee") );
	}
}
