
#include <python.h>

// Function to deserialize the Python dictionary
PyObject* load_keyboard_mapping(const char* filename) {
    PyObject *pModule, *pFunc, *pArgs, *pValue;
vgfvf
    // Initialize Python interpreter
    Py_Initialize();

    // Load the Python module
    pModule = PyImport_ImportModule("pickle");

    // Get the function from the module
    pFunc = PyObject_GetAttrString(pModule, "load");

    // Create arguments to pass to the function
    pArgs = PyTuple_New(1);
    PyTuple_SetItem(pArgs, 0, PyUnicode_FromString(filename));

    // Call the function with arguments
    pValue = PyObject_CallObject(pFunc, pArgs);

    // Clean up
    Py_DECREF(pModule);
    Py_DECREF(pFunc);
    Py_DECREF(pArgs);

    // Check for errors
    if (pValue == NULL) {
        PyErr_Print();
        return NULL;
    }

    // Return the deserialized dictionary
    return pValue;
}
