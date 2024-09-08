#include <cs50.h>
#include <stdio.h>

typedef struct
{
    string name;
    int votes;
}
candidate;

candidate get_candidate(string prompt);

int main(void)
{
    // candidate person = get_candidate("Enter a Candidate");
    // printf("%s\n", person.name);
    // printf("%i\n", person.votes);

    ///////////////////can also use array
    candidate candidate_array[3];
    for (int i = 0; i < 3; i++)
    {
        candidate_array[i] = get_candidate("Enter a Candidate");
    }

    printf("%s\n", candidate_array[0].name);
    printf("%i\n", candidate_array[1].votes);
    // printf("%i\n", candidate_array[2]);
}

//function to get candidate (like get_int) prompt is what will appear in command console
candidate get_candidate(string prompt)
{
    printf("%s\n", prompt);
    candidate c;
    c.name = get_string("Name: ");
    c.votes = get_int("Votes: ");
    return c;co
}

