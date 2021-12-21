#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if single or doubly list
 * @list: pointer to list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *temp = list;

	if (list == NULL)
		return (1);

	while (temp != NULL)
	{
		if (temp->next == list)
			return (1);
		temp = temp->next;
	}
	return (0);
}
