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

    if (head == NULL || *head == NULL)
        return (1);


    while (temp)
    {
        temp = temp->next;
        len++;
    }


    arr = malloc(sizeof(int) * len);
    if (!arr)
        return (0);

    temp = *head;


    for (i = 0; i < len; i++)
    {
        arr[i] = temp->n;
        temp = temp->next;
    }


    if (pal(arr, 0, len - 1) == 1)
    {
        free(arr);
        return (1);
    }

    free(arr);
    return (0);
}
