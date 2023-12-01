#include <iostream>
#include <vector>

int main() {
    int casos;
    std::cin >> casos;

    for (int caso = 1; caso <= casos; caso++) {
        int M;
        std::cin >> M;
        
        if (M == 0) {
            std::cout << "Caso " << caso << ":" << std::endl;
            std::cout << "Empty case!" << std::endl;
            continue;
        }

        std::vector<int> somas(M, 0);

        for (int i = 0; i < M; i++) {
            int a, b, c;
            std::cin >> a >> b >> c;
            somas[i] = a + b + c;
        }

        std::cout << "Caso " << caso << ":" << std::endl;
        for (int i = 0; i < M; i++) {
            std::cout << somas[i] << std::endl;
        }
    }

    return 0;
}