#include <Python.h>
#include <stdio.h>

static void print_bytes_info(PyObject *p, const char *indent)
{
	PyBytesObject *bytes;
	Py_ssize_t size;
	Py_ssize_t shown;
	Py_ssize_t i;
	unsigned char *data;

	if (!PyBytes_Check(p))
	{
		printf("%s[.] bytes object info\n", indent);
		printf("%s  [ERROR] Invalid Bytes Object\n", indent);
		return;
	}
	bytes = (PyBytesObject *)p;
	size = bytes->ob_base.ob_size;
	data = (unsigned char *)bytes->ob_sval;
	shown = size < 9 ? size + 1 : 10;
	printf("%s[.] bytes object info\n", indent);
	printf("%s  size: %ld\n", indent, (long int)size);
	printf("%s  trying string: %s\n", indent, bytes->ob_sval);
	printf("%s  first %ld bytes:", indent, (long int)shown);
	for (i = 0; i < shown; i++)
		printf(" %02x", data[i]);
	printf("\n");
}

/**
 * print_python_list - prints information about a Python list
 * @p: Python object expected to be a list
 */
void print_python_list(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t size;
	Py_ssize_t i;
	PyObject *item;

	list = (PyListObject *)p;
	size = list->ob_base.ob_size;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", (long int)size);
	printf("[*] Allocated = %ld\n", (long int)list->allocated);
	for (i = 0; i < size; i++)
	{
		item = list->ob_item[i];
		printf("Element %ld: %s\n", (long int)i,
			item->ob_type->tp_name);
		if (PyBytes_Check(item))
			print_bytes_info(item, "");
	}
}

/**
 * print_python_bytes - prints information about a Python bytes object
 * @p: Python object expected to be bytes
 */
void print_python_bytes(PyObject *p)
{
	print_bytes_info(p, "");
}
