#include "lists.h"
/**
 * insert_node - inserts a number and sorts it in a linked list
 * @head: pointer to the first node (head)
 * @number: number to insert in the new node
 *
 * Return: pointer to the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *p = *head;

	if (new == NULL)
		return (NULL);

	new->n = number;

	if (number <= p->n || p == NULL)
	{
		new->next = p;
		*head = new;
		return (new);
	}

	while (p != NULL && p->next != NULL && p->next->n <= number)
		p = p->next;
	new->next = p->next;
	p->next = new;
	return (new);

}
