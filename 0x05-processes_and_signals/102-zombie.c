#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * main - Create zombie processes
 *
 * Description: Create five zombie processes

 * Return: Always 0.
 */

int main(void)
{
	int zombie;
	pid_t couzom;

	zombie = 0;
	while (zombie < 5)
	{
		couzom = fork();
		if (couzom)
			printf("Zombie process created, PID: %i\n", couzom);
		else
			exit(0);
		zombie++;
	}
	sleep(100);
	return (0);
}
