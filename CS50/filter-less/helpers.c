#include "helpers.h"
#include <math.h>
#define RED_COLOR 0
#define GREEN_COLOR 1
#define BLUE_COLOR 2

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column < width; column++)
        {
            int rgbGrey = round((image[row][column].rgbtBlue + image[row][column].rgbtGreen + image[row][column].rgbtRed) / 3);

            image[row][column].rgbtBlue = rgbGrey;
            image[row][column].rgbtGreen = rgbGrey;
            image[row][column].rgbtRed = rgbGrey;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column < width; column++)
        {
            int sepiaRed = round(0.393 * image[row][column].rgbtRed + 0.769 * image[row][column].rgbtGreen + 0.189 * image[row][column].rgbtBlue);
            int sepiaGreen = round(0.349 * image[row][column].rgbtRed + 0.686 * image[row][column].rgbtGreen + 0.168 * image[row][column].rgbtBlue);
            int sepiaBlue = round(0.272 * image[row][column].rgbtRed + 0.534 * image[row][column].rgbtGreen + 0.131 * image[row][column].rgbtBlue);

            image[row][column].rgbtRed = fmin(255, sepiaRed);
            image[row][column].rgbtGreen = fmin(255, sepiaGreen);
            image[row][column].rgbtBlue = fmin(255, sepiaBlue);
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE buff;
    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column < width / 2; column++)
        {
            buff = image[row][column];
            image[row][column] = image[row][width - column - 1];
            image[row][width - column - 1] = buff;
        }
    }
    return;
}


int get_blur(int i, int j, int height, int width, RGBTRIPLE image[height][width], int color_pos)
{
    float x = 0;
    int sum = 0;
    for (int row = i - 1; row <= (i + 1); row++)
    {
        for (int column = j - 1; column <= (i + 1); column++)
        {
            if (row < 0 || row >= height || column < 0 || column >= width)
            {
                continue;
            }
            if (color_pos == RED_COLOR)
            {
                sum += image[row][column].rgbtRed;
            }
            else if (color_pos == GREEN_COLOR)
            {
                sum += image[row][column].rgbtGreen;
            }
            else if (color_pos == BLUE_COLOR)
            {
                sum += image[row][column].rgbtBlue;
            }
            x++;
        }
    }
    return round(sum / x);
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column < width / 2; column++)
        {
            copy[row][column] = image[row][column];
        }
    }

    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column < width / 2; column++)
        {
            image[row][column].rgbtRed = get_blur(row, column, height, width, copy, RED_COLOR);
            image[row][column].rgbtGreen = get_blur(row, column, height, width, copy, GREEN_COLOR);
            image[row][column].rgbtBlue = get_blur(row, column, height, width, copy, BLUE_COLOR);
        }
    }
    return;
}

