// Using LD_PRELOAD and compiling into shared object, 32-bit gcc
// This was quite challenging for me as I haven't played with OS stuff much, however 
// after research, it's quite easy to write a solution

#include <unistd.h>
#include <sys/types.h>

uid_t geteuid(void) {

  unsigned int devil_number = 666;
  return devil_number;
  
}

// The compile is quite long and takes a while to get right: gcc -shared solve.c -fPIC -m32 -rdynamic -g -o solve.so
