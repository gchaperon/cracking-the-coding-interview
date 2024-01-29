#include <cmath>
#include <iostream>
#include <set>
#include <cstring>
#include <catch2/catch_test_macros.hpp>

bool is_unique( const char s[] ) {
	std::set<char> unique;
	const char *p = s;
	char c = *p;
	while ((c = *p++) != '\0') {
	    unique.insert(c);
	}
	return unique.size() == strlen(s);
}

bool is_unique_no_data_structure( const char s[] ) {
	bool seen[ 1 << (sizeof(char) * 8) ] = { false };

	unsigned char c;
	while ((c = *s++) != '\0') {
		if (seen[c]) return false;
		seen[c] = true;
	}
	return true;
}

typedef bool (*Fn) (const char*);

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


