#include <string>
#include <catch2/catch_test_macros.hpp>


bool is_substring(std::string s1, std::string s2) {
	return s2.find(s1) != std::string::npos;
}


bool is_rotation(std::string s1, std::string s2) {
	return s1.size() == s2.size() && is_substring(s1, s2 + s2);
}


TEST_CASE( "Checks rotation" ) {
	REQUIRE( is_rotation("", "") );
	REQUIRE( is_rotation("waterbottle", "erbottlewat") );
	REQUIRE( is_rotation("ottlewaterb", "erbottlewat") );
	REQUIRE( !is_rotation("asdfwaterbottle", "erbottlewat") );
	REQUIRE( !is_rotation("wat", "erbottlewat") );
	REQUIRE( !is_rotation("lewaterbottle", "erbottlewat") );
}
