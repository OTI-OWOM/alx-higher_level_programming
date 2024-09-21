#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
if (!PyList_Check(p)) {
printf("Invalid List Object\n");
return;
}
    
Py_ssize_t size = PyList_Size(p);
printf("[*] Python list info\n");
printf("[*] Size of the Python List = %zd\n", size);
printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

for (Py_ssize_t i = 0; i < size; i++) {
PyObject *item = PyList_GetItem(p, i);
const char *type = Py_TYPE(item)->tp_name;
printf("Element %zd: %s\n", i, type);
}
}

void print_python_bytes(PyObject *p) {
if (!PyBytes_Check(p)) {
printf("Invalid Bytes Object\n");
return;
}
    
Py_ssize_t size = PyBytes_Size(p);
printf("[*] Python bytes info\n");
printf("[*] Size of the Python Bytes = %zd\n", size);
    
printf("[*] First %zd bytes: ", size > 10 ? 10 : size);
for (Py_ssize_t i = 0; i < (size > 10 ? 10 : size); i++) {
printf("%02x ", (unsigned char)PyBytes_AsString(p)[i]);
}
printf("\n");
}
