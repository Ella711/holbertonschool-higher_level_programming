#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * checkPalindrome - recursive function to check for palindrome
 * @start: pointer to start of list
 * @end: pointer at end of list
 * Return: 0 or 1.
 */
int checkPalindrome(listint_t **start, listint_t *end)
{
	if (end == NULL)
		return (1);

	if (checkPalindrome(start, end->next) && ((*start)->n == end->n))
	{
		*start = (*start)->next;
		return (1);
	}
	return (0);
}

/**
 * is_palindrome - check if list is palindrome
 * @head: pointer to start of list
 * Return: 0 or 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *start = *head;
	listint_t *end = *head;

	if (head == NULL)
		return (0);
	if (*head == NULL) /* one node list is palindrome */
		return (1);
	return (checkPalindrome(&start, end));
}

