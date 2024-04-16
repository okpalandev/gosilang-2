#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "translation.h" 

int main() {
    FILE *file;
    unsigned char buffer[1024];
    size_t bytesRead;

    // Open the pickled file
    file = fopen("../dist/keyboard_mapping.pkl", "rb");
    if (file == NULL) {
        fprintf(stderr, "Error opening file\n");
        return 1;
    }

    // Read the file contents into a buffer
    bytesRead = fread(buffer, 1, sizeof(buffer), file);
    if (bytesRead == 0) {
        fprintf(stderr, "Error reading file\n");
        fclose(file);
        return 1;
    }

    fclose(file);

    // Deserialize the Python dictionary
    PyObject *pDict = load_keyboard_mapping("../dist/keyboard_mapping.pkl");
    if (pDict == NULL) {
        fprintf(stderr, "Error loading keyboard mappings\n");
        return 1;
    }


    // Clean up Python objects
    Py_DECREF(pDict);

    return 0;
}
