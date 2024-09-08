#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

string text;

int count_letters(string input);
int count_words(string input);
int count_sentences(string input);


int main(void)
{
    // Get input
    text = get_string("Text: ");

    //find characters, words and sentences
    int characters = count_letters(text);
    // printf("%i\n", characters);

    int word = count_words(text);
    // printf("%i\n", word);

    int sentence = count_sentences(text);
    // printf("%i\n", sentence);

    //calculate index
    float L = (float) characters / (float) word * 100;
    float S = (float) sentence / (float) word * 100;

    int index = round(0.0588 * L - 0.296 * S - 15.8);

    // print result
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);

    }
}

int count_letters(string input)
{
    int letters = 0;
    int i = 0;
    while (text[i] != '\0')
    {
        if isalpha(text[i])
        {
            letters++;
            i++;
        }
        else
        {
            i++;
        }
    }
    return letters;
}

int count_words(string input2)
{
    int words = 1;
    int n = 0;
    while (text[n] != '\0')
    {
        if (text[n] == ' ')
        {
            words++;
            n++;
        }
        else
        {
            n++;
        }
    }
    return words;
}

int count_sentences(string input3)
{
    int sentences = 0;
    int x = 0;
    while (text[x] != '\0')
    {
        if (text[x] == '.' || text[x] == '?' || text[x] == '!')
        {
            sentences++;
            x++;
        }
        else
        {
            x++;
        }
    }
    return sentences;
}