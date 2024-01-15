#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if lists contains a cycle
 * @lists: list to check
 *
 * Return: if there is no cycle then 0 else 1
 */

int check_cycle(listint_t *list)
{
	listint_t *s, *f;

	if (list == NULL || list->next == NULL)
		return (0);

	s = list->next;
	f = list->next->next;

	while (s && f && f->next)
	{
		if (s == f)
			return (1);
		s = s->next;
		f = f->next->next;
	}
	return (0);
}
