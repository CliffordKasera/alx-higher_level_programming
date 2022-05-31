#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: list head
 * @number: number to store in the new node
 * Return: pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *start;
	listint_t *step;

	start = *head;

	step = malloc(sizeof(listint_t));
	if (step == NULL)
		return (NULL);
	step->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		step->next = *head;
		*head = step;
		return (step);
	}
	while (start->next != NULL)
	{
		if ((start->next)->n >= number)
		{
			step->next = start->next;
			start->next = step;
			return (step);
		}
		start = start->next;
	}
	start->next = NULL;
	start->next = step;
	return (step);
}
