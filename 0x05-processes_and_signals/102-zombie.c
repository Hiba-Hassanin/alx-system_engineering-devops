#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>

/**
 * main - zombies
 *
 * Description: a program that creates 5 zombie.

 * Return: 0 if successful
 */

int main(void)
{
	int i;
	pid_t pidme;

	i = 0;
	while (i < 5)
	{
		pidme = fork();
		if (pidme)
			printf("Zombie process created, PID: %i\n", pidme);
		else
			exit(0);
		i++;
	}
	sleep(100);
	return (0);
}
