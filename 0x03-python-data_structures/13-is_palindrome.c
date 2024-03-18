#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: beginning of list
 *
 * Return: 0 if not a palindrome and 1 if it is
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL || *(head)->next == NULL)
		return (1);

	int i = 0;
	int sum1 = 0, sum2 = 0;
	listint_t *p1 = *head;
	listint_t *p2 = *head;

	while (p1 != NULL)
	{
		i++;
		p1 = p1->next;
	}
	p1 = *head;
	if (i % 2 != 0)
		return (0);
	i = i / 2;
	while (i > 0)
	{
		p1 = p1->next;
		i--;
	}

	while (p1 != NULL)
	{
		sum1 = sum1 + p1->n;
		sum2 = sum2 + p2->n;
		p1 = p1->next;
		p2 = p2->next;
	}
	if (sum1 == sum2)
		return (1);
	return (0);
}
