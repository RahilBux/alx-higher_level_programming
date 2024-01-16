#include "lists.h"

/**
 * insert_node - inserts a number in a linked list
 * @head: A pointer to the head
 * @number: number to insert
 * 
 * Return: 0 if failure or pointer to node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *no = *head, *ne;

	ne = malloc(sizeof(listint_t));
	if (ne == NULL)
		return (NULL);
	ne->n = number;

	if (no == NULL || no->n >= number)
	{
		ne->next = no;
		*head = ne;
		return (ne);
	}

	while (no && no->next && no->next->n < number)
		no = no->next;

	ne->next = no->next;
	no->next = ne;

	return (ne);
}
