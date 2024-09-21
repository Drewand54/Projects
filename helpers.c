#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int avg = 0;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            avg = (int) round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0);
            image[i][j].rgbtBlue = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtRed = avg;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int originalRed;
    int originalGreen;
    int originalBlue;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            originalRed = image[i][j].rgbtRed;
            originalGreen = image[i][j].rgbtGreen;
            originalBlue = image[i][j].rgbtBlue;
            if ((.272 * originalRed + .534 * originalGreen + .131 * originalBlue) <= 255)
            {
                image[i][j].rgbtBlue = round(.272 * originalRed + .534 * originalGreen + .131 * originalBlue);
            }
            else
            {
                image[i][j].rgbtBlue = 255;
            }
            if ((.349 * originalRed + .686 * originalGreen + .168 * originalBlue) <= 255)
            {
                image[i][j].rgbtGreen = round(.349 * originalRed + .686 * originalGreen + .168 * originalBlue);
            }
            else
            {
                image[i][j].rgbtGreen = 255;
            }
            if ((.393 * originalRed + .769 * originalGreen + .189 * originalBlue) <= 255)
            {
                image[i][j].rgbtRed = round(.393 * originalRed + .769 * originalGreen + .189 * originalBlue);
            }
            else
            {
                image[i][j].rgbtRed = 255;
            }
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            temp = image[i][j];
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 - j] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    int avgRed;
    int avgGreen;
    int avgBlue;
    int count;
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            avgRed = 0;
            avgGreen = 0;
            avgBlue = 0;
            count = 0;
            if ((i - 1 >= 0 && i - 1 < height) && (j - 1 >= 0 && j - 1 < width))
            {
                avgRed = avgRed + copy[i - 1][j - 1].rgbtRed;
                avgGreen = avgGreen + copy[i - 1][j - 1].rgbtGreen;
                avgBlue = avgBlue + copy[i - 1][j - 1].rgbtBlue;
                count++;
            }
            if ((i - 1 >= 0 && i - 1 < height) && (j >= 0 && j < width))
            {
                avgRed = avgRed + copy[i - 1][j].rgbtRed;
                avgGreen = avgGreen + copy[i - 1][j].rgbtGreen;
                avgBlue = avgBlue + copy[i - 1][j].rgbtBlue;
                count++;
            }
            if ((i - 1 >= 0 && i - 1 < height) && (j + 1 >= 0 && j + 1 < width))
            {
                avgRed = avgRed + copy[i - 1][j + 1].rgbtRed;
                avgGreen = avgGreen + copy[i - 1][j + 1].rgbtGreen;
                avgBlue = avgBlue + copy[i - 1][j + 1].rgbtBlue;
                count++;
            }
            if ((i >= 0 && i < height) && (j - 1 >= 0 && j - 1 < width))
            {
                avgRed = avgRed + copy[i][j - 1].rgbtRed;
                avgGreen = avgGreen + copy[i][j - 1].rgbtGreen;
                avgBlue = avgBlue + copy[i][j - 1].rgbtBlue;
                count++;
            }
            if ((i >= 0 && i < height) && (j >= 0 && j < width))
            {
                avgRed = avgRed + copy[i][j].rgbtRed;
                avgGreen = avgGreen + copy[i][j].rgbtGreen;
                avgBlue = avgBlue + copy[i][j].rgbtBlue;
                count++;
            }
            if ((i >= 0 && i < height) && (j + 1 >= 0 && j + 1 < width))
            {
                avgRed = avgRed + copy[i][j + 1].rgbtRed;
                avgGreen = avgGreen + copy[i][j + 1].rgbtGreen;
                avgBlue = avgBlue + copy[i][j + 1].rgbtBlue;
                count++;
            }
            if ((i + 1 >= 0 && i + 1 < height) && (j - 1 >= 0 && j - 1 < width))
            {
                avgRed = avgRed + copy[i + 1][j - 1].rgbtRed;
                avgGreen = avgGreen + copy[i + 1][j - 1].rgbtGreen;
                avgBlue = avgBlue + copy[i + 1][j - 1].rgbtBlue;
                count++;
            }
            if ((i + 1 >= 0 && i + 1 < height) && (j >= 0 && j < width))
            {
                avgRed = avgRed + copy[i + 1][j].rgbtRed;
                avgGreen = avgGreen + copy[i + 1][j].rgbtGreen;
                avgBlue = avgBlue + copy[i + 1][j].rgbtBlue;
                count++;
            }
            if ((i + 1 >= 0 && i + 1 < height) && (j + 1 >= 0 && j + 1 < width))
            {
                avgRed = avgRed + copy[i + 1][j + 1].rgbtRed;
                avgGreen = avgGreen + copy[i + 1][j + 1].rgbtGreen;
                avgBlue = avgBlue + copy[i + 1][j + 1].rgbtBlue;
                count++;
            }

            image[i][j].rgbtRed = round((avgRed / (double) count));
            image[i][j].rgbtGreen = round((avgGreen / (double) count));
            image[i][j].rgbtBlue = round((avgBlue / (double) count));
        }
    }
    return;
}
