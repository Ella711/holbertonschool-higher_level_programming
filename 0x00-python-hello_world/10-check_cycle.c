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
	listint_t *slow = list, *fast = list->next;

	if (list == NULL)
		return (0);

	while (list->next != NULL)
	{
		if (fast == NULL || fast->next == NULL)
			return (0);
		if (slow == fast || fast->next == slow)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
