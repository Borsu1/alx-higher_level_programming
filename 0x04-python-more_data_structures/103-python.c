#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
    long int size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
    for (long int i = 0; i < size; i++)
    {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, item->ob_type->tp_name);
    }
}

void print_python_bytes(PyObject *p)
{
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }
    long int size = PyBytes_Size(p);
    char *str = PyBytes_AsString(p);
    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);
    if (size < 10)
        printf("  first %ld bytes: ", size);
    else
        printf("  first 10 bytes: ");
    for (long int i = 0; i < size && i < 10; i++)
    {
        printf("%02hhx%s", str[i], i + 1 < size && i + 1 < 10 ? " " : "\n");
    }
}
