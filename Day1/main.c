#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    FILE *file;
    char line[10];
    char directions = malloc(sizeof(char[10, 5000]));
    int count_arr = 0;

    file = fopen("Day1/input.txt", "r");

    if (file == NULL) {
        perror("Error Opening File");
        return 1;
    }

    while (fscanf(file, "%s", &line)){
        directions[count_arr] = line;
        count_arr++;
        printf("%s\n", line);
    }

    return 0;
}