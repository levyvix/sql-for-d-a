#include <iostream>

// Função para calcular o MDC usando o algoritmo de Euclides
int calcularMDC(int a, int b)
{
    int R = 0;
    while (b > 0)
    {
        R = a % b;
        a = b;
        b = R;
    }
    return a;
}

int main()
{
    int casos;
    std::cin >> casos;

    for (int i = 1; i <= casos; i++)
    {
        int numFileiras;
        std::cin >> numFileiras;

        std::cout << "Caso " << i << ":" << std::endl;

        for (int j = 0; j < numFileiras; j++)
        {
            int a, b;
            std::cin >> a >> b;

            int mdc = calcularMDC(a, b);
            std::cout << mdc << std::endl;
        }
    }

    return 0;
}