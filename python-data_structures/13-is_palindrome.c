#include "lists.h"

/**
 * reverse_list - reverses a singly linked list
 * @head: first node in the list
 * Return: pointer to the first node after reversal
 */
static listint_t *reverse_list(listint_t *head)
{
	listint_t *previous = NULL;
	listint_t *next;

	while (head != NULL)
	{
		next = head->next;
		head->next = previous;
		previous = head;
		head = next;
	}
	return (previous);
}

/**
 * is_palindrome - checks whether a singly linked list reads the same both ways
 * @head: address of the list head
 * Return: 1 if the list is a palindrome, otherwise 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow;
	listint_t *fast;
	listint_t *right;
	listint_t *left;
	int result = 1;

	if (head == NULL || *head == NULL)
		return (1);
	slow = *head;
	fast = *head;
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	if (fast != NULL)
		slow = slow->next;
	right = reverse_list(slow);
	left = *head;
	fast = right;
	while (fast != NULL)
	{
		if (left->n != fast->n)
			result = 0;
		left = left->next;
		fast = fast->next;
	}
	reverse_list(right);
	return (result);
}
