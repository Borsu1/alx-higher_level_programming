#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev, *tmp;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
	return (1);
	while (fast != NULL && fast->next != NULL)
	{
	fast = fast->next->next;
	prev = slow;
	slow = slow->next;
	}
	prev->next = NULL;
	prev = NULL;
	while (slow != NULL)
	{
	tmp = slow->next;
	slow->next = prev;
	prev = slow;
	slow = tmp;
	}
	while (*head != NULL)
	{
	if ((*head)->n != prev->n)
	return (0);
	*head = (*head)->next;
	prev = prev->next;
	}
	return (1);
}

