#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - insert a node in a sorted list
 * @head: pointer to head of list
 * @number: data to store on new node
 * Return: head.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = NULL, *new_node = NULL;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (*head);
	}
	else
	{
		current = *head;
		while (current->next != NULL && current->next->n < new_node->n)
			current = current->next;
		new_node->next = current->next;
		current->next = new_node;

	}
	return (*head);
}

