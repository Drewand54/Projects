// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 17602;

int words = 0;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int index = hash(word);
    words--;
    node *ptr = table[index];

    while (ptr != NULL)
    {
        if (strcasecmp(ptr->word, word) == 0)
        {
            return true;
        }
        else
        {
            ptr = ptr->next;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    if (isalpha(word[1]) == 0)
    {
        words++;
        return ((toupper(word[0]) - 'A') * 676);
    }
    else if (isalpha(word[2]) == 0)
    {
        words++;
        return ((toupper(word[0]) - 'A') * 676) + ((toupper(word[1]) - 'A' + 1));
    }
    else
    {
        words++;
        return (((toupper(word[0]) - 'A') * 676) + ((toupper(word[1]) - 'A' + 1) * 26) + (toupper(word[2]) - 'A' + 1));
    }
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    int index = 0;
    char word[LENGTH];
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }

    while (fscanf(file, "%s", word) != EOF)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;
        }
        strcpy(n->word, word);
        index = hash(word);
        n->next = table[index];
        table[index] = n;
    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return words;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        node *ptr = table[i];
        while (ptr != NULL)
        {
            node *cursor = ptr->next;
            free(ptr);
            ptr = cursor;
        }
    }
    return true;
}
