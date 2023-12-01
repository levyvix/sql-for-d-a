#include <iostream>
#include <vector>

// Função para encontrar o valor máximo em um array
int encontrarMaximo(const std::vector<int> &array)
{
    int max = array[0];
    for (int i = 1; i < array.size(); i++)
    {
        if (array[i] > max)
        {
            max = array[i];
        }
    }
    return max;
}

int main()
{
    int casos;
    std::cin >> casos;

    for (int caso = 1; caso <= casos; caso++)
    {
        int numElementos;
        std::cin >> numElementos;

        std::vector<int> array(numElementos);

        for (int i = 0; i < numElementos; i++)
        {
            std::cin >> array[i];
        }

        int maximo = encontrarMaximo(array);

        std::cout << "Case " << caso << ":" << std::endl;
        std::cout << maximo << std::endl;
    }

    return 0;
}
