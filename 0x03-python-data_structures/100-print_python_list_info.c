#include <Python.h>
/**
 * print_python_list_info - prints info about Python lists
 * @p: PyObj list
 */

void print_python_list_info(PyObject *p)
{
	int s, allo, i;
	PyObject *ob;

	s = Py_SIZE(p);
	allo = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", allo);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		ob = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(ob)->tp_name);
	}
}
