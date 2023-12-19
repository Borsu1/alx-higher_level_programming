#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints information about Python lists
 * @p: A pointer to the Python list object
 *
 * Description: This function takes a Python list object as input and prints
 * information about the list and its elements. This is useful for debugging
 * or understanding the structure of Python lists.
 */
void print_python_list(PyObject *p)
{
	if (PyList_Check(p))
	{
	Py_ssize_t size = PyList_GET_SIZE(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (Py_ssize_t i = 0; i < size; i++)
	{
	PyObject *item = PyList_GET_ITEM(p, i);

	printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
	}
	else
	{
	printf("  [ERROR] Invalid List Object\n");
	}
}

/**
 * print_python_bytes - Prints information about Python bytes objects
 * @p: A pointer to the Python bytes object
 *
 * Description: This function takes a Python bytes object as input and prints
 * information about the bytes object. This can be useful for debugging or
 * understanding the structure of Python bytes objects.
 */
void print_python_bytes(PyObject *p)
{
	if (PyBytes_Check(p))
	{
	char *s = PyBytes_AS_STRING(p);
	Py_ssize_t size = PyBytes_GET_SIZE(p);

	printf("[*] Python bytes\n");
	printf("  Size of the Python Bytes = %ld\n", size);
	printf("  Trying string: %s\n", s);
	printf("  First 10 bytes:");
	for (Py_ssize_t i = 0; i < size && i < 10; i++)
	{
	printf(" %02hhx", s[i]);
	}
	printf("\n");
	}
	else
	{
	printf("  [ERROR] Invalid Bytes Object\n");
	}
}

/**
 * print_python_float - Prints information about Python float objects
 * @p: A pointer to the python float object
 * Description: This function takes a Python float object as input and prints
 * information about the float object. This can be useful for debugging or
 * understanding the structure of Python float objects.
 */
void print_python_float(PyObject *p)
{
	if (PyFloat_Check(p))
	{
	double value = PyFloat_AsDouble(p);

	printf("[*] Python float\n");
	printf("  Value: %0.15g\n", value);
	}
	else
	{
	printf("  [ERROR] Invalid Float Object\n");
	}
}
