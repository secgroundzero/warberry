#include <stdio.h>

int main(int argc, char *argv[]){
    FILE *fp;
    fp = fopen("movies.dat","r");
    if(fp == NULL{
        printf("Error: can't open file to read\n");
        return -1;
    }

    // implied else, fopen successful

    printf("File people.dat opened successfully to read\n");

    while ( 1 == fread( &key, 4, 1, fp ) )
    {
       int bufFirst[4] = {'\0'};

      // use  lengths to determine how much more  bytes to read for each field
      result = fread( bufFirst, key.first, 1, fp );
      printf("%s\n", result);
    }

    fclose(fp);
    return 0; 


}

