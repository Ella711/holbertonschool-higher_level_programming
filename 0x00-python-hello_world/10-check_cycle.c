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
	if (list == NULL || list->next == NULL)
		return (0);

	while (list && list->next)
	{
		if (list->next >= list || !list->next)
			break;

		list = list->next;
	}
	if (list->next)
		return (1);

	return (0);
}

