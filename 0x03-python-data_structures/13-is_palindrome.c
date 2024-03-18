#include "lists.h"

/**
 * rev_listint - reverses a linked list
 * @head: pointer to first node
 */

void rev_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *next = NULL;
	listint_t *current = *head;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}

/**
 * is_palindrome - checks if linked list is a palindrome
 * @head: pointer to head
 *
 * Return: 1 if its a palindrome and 0 if not
 */

int is_palindrome(listint_t **head)
{
	listint_t *s = *head, *f = *head, *temp = *head, *dup = NULL;

	if (*head == NULL)
		return (1);

	while (1)
	{
		f = f->next->next;
		if (f == NULL)
		{
			dup = s->next;
			break;
		}
		if (f->next == NULL)
		{
			dup = s->next->next;
			break;
		}
		s = s->next;
	}
	rev_listint(&dup);

	while (dup != NULL && temp != NULL)
	{
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
			return (0);
	}
	if (dup == NULL)
		return (1);

	return (0);
}
