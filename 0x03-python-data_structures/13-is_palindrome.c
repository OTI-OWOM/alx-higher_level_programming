#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * pal - check if a list is palindrome (array version)
 * @arr: pointer to array
 * @index_a: first index
 * @index_b: second index
 * Return: 1 if palindrome, 0 otherwise
 */
int pal(int *arr, int index_a, int index_b)
{
    if (index_a >= index_b)
        return (1);
    if (arr[index_a] != arr[index_b])
        return (0);
    return (pal(arr, index_a + 1, index_b - 1));
}

/**
 * is_palindrome - check if a singly linked list is a palindrome
 * @head: pointer to node listint_t
 * Return: 1 if list is palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    int len = 0, i = 0;
    const listint_t *temp = *head;
    int *arr;

    if (head == NULL || *head == NULL)  // Handle NULL head or empty list
        return (1);

    // Count the length of the list
    while (temp)
    {
        temp = temp->next;
        len++;
    }

    // Create an array to store the list values
    arr = malloc(sizeof(int) * len);
    if (!arr)
        return (0);  // Memory allocation failed

    temp = *head;

    // Copy the list values into the array
    for (i = 0; i < len; i++)
    {
        arr[i] = temp->n;
        temp = temp->next;
    }

    // Check if the list is a palindrome
    if (pal(arr, 0, len - 1) == 1)
    {
        free(arr);
        return (1);
    }

    free(arr);
    return (0);
}
