#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * infinite_while - an infinite loop is created
 * to make the program hang
 * Return: 0 (Success)
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - 5 zombie processes are created
 * Return: 0 (Success)
 */
int main(void)
{
	int j;
	pid_t zombie;

	for (j = 0; j < 5; j++)
	{
		zombie = fork();
		if (!zombie)
			return (0);
		printf("Zombie process created, PID: %d\n", zombie);
	}

	infinite_while();
	return (0);
}
