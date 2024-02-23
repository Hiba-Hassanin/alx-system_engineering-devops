#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

/**
 * main - Create zombie processes
 *
 * Description: Create five zombie processes
 * Return: Always 0.
 */

int main(void)
{
    int i;
    pid_t pidme;

    i = 0;
    while (i < 5)
    {
        pidme = fork();
        if (pidme > 0)
            printf("Zombie process created, PID: %i\n", pidme);
        else if (pidme == 0)
            exit(0);
        else
        {
            perror("fork");
            return (1);
        }
        i++;
    }

    sleep(100); /* Sleep to keep the parent process alive */
    return (0);
}
