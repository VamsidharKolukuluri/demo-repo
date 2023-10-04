#include <vector>
#include <iostream>
using namespace std;
using std::vector;

long long factorial(long long n)
{
    if (n <= 0)
        return 1;
    return factorial(n - 1) + factorial(n - 2);
}

vector<long long> factorialNumbers(long long n)
{
    // Write Your Code Here
    vector<long long> v;
    for (int i = 0; i < n / 2; i++)
    {
        int result = factorial(i);
        if (result < n)
        {
            v.push_back(result);
        }
    }
    return v;
}