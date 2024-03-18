#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * rev_listint - reverses a linked list
 * @head: pointer to first node of list
 *
 */

void rev_listint(listint_t **head)
{
	listint_t *next = NULL;
	listint_t *prev = NULL;
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
 * create_node - creates a node
 * @data: integer to insert to new node
 *
 * Return: pointer to new node
 */

listint_t *create_node(int data)
{
	listint_t *newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
	{
		printf("Error allocating memory\n");
		exit(1);
	}
	newnode->n = data;
	newnode->next = NULL;
	return (newnode);
}

/**
 * dup_list - duplicates a singly linked list
 * @original: pointer to the original list
 *
 * Return: pointer to the duplicate list
 */

listint_t *dup_list(listint_t *original)
{
	if (original == NULL)
		return (NULL);

	listint_t *newhead = create_node(original->n);

	listint_t *curroriginal = original->next;
	listint_t *currnew = newhead;

	while (curroriginal != NULL)
	{
		currnew->next = create_node(curroriginal->n);
		curroriginal = curroriginal->next;
		currnew = currnew->next;
	}
	return (newhead);
}

/**
 * free_list - frees a linked list
 * @head: pointer to the first node
 */

void free_list(listint_t *head)
{
	listint_t *temp;
	while (head != NULL)
	{
		temp = head;
		head = head->next;
		free(temp);
	}
}

/**
 * is_palindrome - checks if linked list is a palindrome
 * @head: pointer to first node
 *
 * Return: 0 if not a palindrome and 1 if it is
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL)
		return (1);
	listint_t *dup = dup_list(*head), *p1 = *head;
	rev_listint(&dup);
	listint_t *p2 = dup;

	while (p1 != NULL)
	{
		if (p1->n != p2->n)
			return (0);
		p1 = p1->next;
		p2 = p2->next;
	}
	free(dup);
	return (1);
}
