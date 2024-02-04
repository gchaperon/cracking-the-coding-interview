#include <string>
#include <catch2/catch_test_macros.hpp>


using namespace std::literals::string_literals;


std::string urlify( std::string str , int length) {
	// assumes enough whitespace at the end to perform inplace
	int nwhite = 0;
	for (int i = 0; i < length; i++) {
		if (str[i] == ' ') {
			nwhite ++;
		}
	}
	int copypos = length - 1 + nwhite * 2;
	for (int i = length - 1; i >= 0; i--) {
		if (str[i] == ' ') {
			for (char c: R"(02%)"s) {
				str[copypos--] = c;
			}
		} else {
			str[copypos--] = str[i];
		}
	}
	return str;
}


TEST_CASE( "Replaces spaces" ) {
	REQUIRE( urlify("Mr John Smith    "s, 13)
		   == R"(Mr%20John%20Smith)" );
	REQUIRE( urlify("Puro Chile es tu cielo azulado          "s, 30)
		   == R"(Puro%20Chile%20es%20tu%20cielo%20azulado)");
	REQUIRE( urlify("  what\tis this      "s, 14)
		   == R"(%20%20what	is%20this)" );
}
