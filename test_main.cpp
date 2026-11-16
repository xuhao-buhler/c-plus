#include <sstream>
#include <string>

#include "unity.h"

int run(std::istream& input, std::ostream& output, std::ostream& error);

void setUp() {}
void tearDown() {}

void test_run_adds_numbers()
{
    std::istringstream input("2 3");
    std::ostringstream output;
    std::ostringstream error;

    TEST_ASSERT_EQUAL_INT(0, run(input, output, error));
    TEST_ASSERT_EQUAL_STRING("Enter two numbers: Their sum is 5\n", output.str().c_str());
    TEST_ASSERT_TRUE(error.str().empty());
}

void test_run_adds_negative_numbers()
{
    std::istringstream input("2 -3");
    std::ostringstream output;
    std::ostringstream error;

    TEST_ASSERT_EQUAL_INT(0, run(input, output, error));
    TEST_ASSERT_EQUAL_STRING("Enter two numbers: Their sum is -1\n", output.str().c_str());
    TEST_ASSERT_TRUE(error.str().empty());
}

void test_run_rejects_invalid_input()
{
    std::istringstream input("2 invalid");
    std::ostringstream output;
    std::ostringstream error;

    TEST_ASSERT_EQUAL_INT(1, run(input, output, error));
    TEST_ASSERT_EQUAL_STRING("Enter two numbers: ", output.str().c_str());
    TEST_ASSERT_EQUAL_STRING("Please enter two valid numbers.\n", error.str().c_str());
}

int main()
{
    UNITY_BEGIN();
    RUN_TEST(test_run_adds_numbers);
    RUN_TEST(test_run_adds_negative_numbers);
    RUN_TEST(test_run_rejects_invalid_input);
    return UNITY_END();
}