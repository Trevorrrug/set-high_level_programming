#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints basic information about a Python list
 * @p: Python object to inspect as a list
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size = list->ob_base.ob_size;
	Py_ssize_t index;

	printf("[*] Size of the Python List = %ld\n", (long int)size);
	printf("[*] Allocated = %ld\n", (long int)list->allocated);
	for (index = 0; index < size; index++)
		printf("Element %ld: %s\n", (long int)index,
			list->ob_item[index]->ob_type->tp_name);
}
