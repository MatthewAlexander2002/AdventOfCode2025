#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    FILE *file;
    char line[10];
    // int count_arr = 0;

    file = fopen("Day1/input.txt", "r");

    if (file == NULL) {
        perror("Error Opening File");
        return 1;
    }

    while (fscanf(file, "%s", &line)){
        char updated_line[10];
        // *updated_line = line[0] + ',' + line[1,10];
        updated_line[0] = (line, updated_line, 0, 1);
        updated_line[1] = ',';
        
    }

    return 0;
}

void slice(const char* str, char* result, size_t start, size_t end) {
    strncpy(result, str+start, end-start);
}