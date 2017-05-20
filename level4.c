// gcc -m32 X.c -o X
// ./X <uID>

#include <sys/ptrace.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/user.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>
#include <stdio.h>
#include <sys/syscall.h>
#include <sys/reg.h>

int main(int argc, char *argv[]) {

    int program = 0;
    int attempt = atoi(argv[1]);
    int current_EAX;
    int pid = fork();
    char *path = "/semtex/semtex4";
    
    if (!pid) {
        ptrace(PTRACE_TRACEME, 0, 0, 0);
        execlp(path, path, 0, NULL);
    } else {
        wait(&program);
        while (1) {
            ptrace(PTRACE_SYSCALL, pid, 0, 0);
            wait(&program);
            if (WIFEXITED(program)) break;

            current_EAX = ptrace(PTRACE_PEEKUSER, pid, 4 * ORIG_EAX, NULL);
            if (current_EAX == SYS_geteuid32) {
                ptrace(PTRACE_POKEUSER, pid, 4 * EAX, attempt);
            }
        }
    }
    return 0;
}

