#!/bin/usr/env bash
#This script creates 5 zombie processes

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <sys/types.h>

/**
 * zombie_processes - function to create 5 zombie processes
 */
void zombie_processes(void)
{
    pid_t child_pid;
    int i;

    for (i = 0; i < 5; i++)
    {
        child_pid = fork();

        if (child_pid == -1)
        {
            perror("fork");
            exit(EXIT_FAILURE);
        }

        if (child_pid == 0)
        {
            printf("Zombie process created, PID: %d\n", getpid());
            exit(EXIT_SUCCESS);
        }
    }

    sleep(10);
}
