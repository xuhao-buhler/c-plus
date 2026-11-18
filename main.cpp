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

int subtract(std::istream& input, std::ostream& output, std::ostream& error)
{
    int firstNumber = 0;
    int secondNumber = 0;

    output << "Enter two numbers: ";
    if (!(input >> firstNumber >> secondNumber))
    {
        error << "Please enter two valid numbers.\n";
        return 1;
    }

    output << "Their difference is " << firstNumber - secondNumber << '\n';
    return 0;
}

#ifndef UNIT_TEST
int main()
{
    int input = -1;
    std::cout << "Choose operation (0 for addition, 1 for subtraction): ";
    if (!(std::cin >> input))
    {
        std::cerr << "Please enter 0 or 1.\n";
        return 1;
    }

    if (input == 0)
    {
        return run(std::cin, std::cout, std::cerr);
    }
    if (input == 1)
    {
        return subtract(std::cin, std::cout, std::cerr);
    }

    std::cerr << "Please enter 0 or 1.\n";
    return 1;
}
#endif
