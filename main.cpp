#include <iostream>

int run(std::istream& input, std::ostream& output, std::ostream& error)
{
    int firstNumber = 0;
    int secondNumber = 0;

    output << "Enter two numbers: ";
    if (!(input >> firstNumber >> secondNumber))
    {
        error << "Please enter two valid numbers.\n";
        return 1;
    }

    output << "Their sum is " << firstNumber + secondNumber << '\n';
    return 0;
}

#ifndef UNIT_TEST
int main()
{
    return run(std::cin, std::cout, std::cerr);
}
#endif
