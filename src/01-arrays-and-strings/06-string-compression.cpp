#include <sstream>
#include <string>
#include <catch2/catch_test_macros.hpp>


std::string compress(std::string str) {
	std::stringstream buf;
	unsigned char blockid = str[0];
	int count = 0;
	for (unsigned char c : str) {
		if (c == blockid) {
			count++;
		} else {
			buf << blockid << count;
			blockid = c;
			count = 1;
		}
	}
	// flush last character block
	buf << blockid << count;
	if (buf.view().size() >= str.size()) {
		return str;
	}
	return buf.str();
}


TEST_CASE( "Compresses" ) {
	REQUIRE( compress("") == "" );
	REQUIRE( compress("abcd") == "abcd" );
	REQUIRE( compress("aabcccccaaa") == "a2b1c5a3" );
}
