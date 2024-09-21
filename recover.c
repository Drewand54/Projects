#include <cs50.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        printf("Could not open file\n");
        return 2;
    }

    typedef uint8_t BYTE;
    BYTE buffer[512];
    char *fileName = malloc(8);
    int images = 0;
    FILE *img = NULL;

    while (fread(buffer, 1, 512, file))
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && ((buffer[3] & 0xf0) == 0xe0))
        {
            if (images > 0)
            {
                fclose(img);
            }
            sprintf(fileName, "%03i.jpg", images);
            img = fopen(fileName, "w");
            images++;
        }
        if (img != NULL)
        {
            fwrite(buffer, 1, 512, img);
        }
    }
    free(fileName);
    fclose(file);
    fclose(img);
    return 0;
}
