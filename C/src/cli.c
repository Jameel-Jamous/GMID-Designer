#include <stdio.h>
#include <string.h>

void process_command(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <command>\n", argv[0]);
        return;
    }

    if (strcmp(argv[1], "hello") == 0) {
        printf("Hello, World!\n");
    } else {
        printf("Unknown command: %s\n", argv[1]);
    }
}

int main(int argc, char *argv[]) {
    process_command(argc, argv);
    return 0;
}

