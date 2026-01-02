#include <cstdint> //unsigned ints
#include <iostream>
#include <stdlib.h>  
#include <cstdio>
#include <string>
#pragma pack(push, 1)

using namespace std;

typedef unsigned short WORD;
typedef unsigned int DWORD;
typedef unsigned int LONG;
typedef unsigned char BYTE;

struct BITMAPFILEHEADER
{
    WORD bfType; //specifies the file type
    DWORD bfSize; //specifies the size in bytes of the bitmap file
    WORD bfReserved1; //reserved; must be 0
    WORD bfReserved2; //reserved; must be 0
    DWORD bfOffBits; //species the offset in bytes from the bitmapfileheader to the bitmap bits
};
struct BITMAPINFOHEADER
{
    DWORD biSize; //specifies the number of bytes required by the struct
    LONG biWidth; //specifies width in pixels
    LONG biHeight; //species height in pixels
    WORD biPlanes; //specifies the number of color planes, must be 1
    WORD biBitCount; //specifies the number of bit per pixel
    DWORD biCompression;//spcifies the type of compression
    DWORD biSizeImage; //size of image in bytes
    LONG biXPelsPerMeter; //number of pixels per meter in x axis
    LONG biYPelsPerMeter; //number of pixels per meter in y axis
    DWORD biClrUsed; //number of colors used by th ebitmap
    DWORD biClrImportant; //number of colors that are important
};

struct PIXEL
{
    // Each value is in range 0 to 255 represented as a byte
    BYTE b; // 1 byte
    BYTE g; // 1 byte
    BYTE r; // 1 byte
};

#pragma pack(pop)

int main(int argc, char *argv[]) { 
    if (argc !=3) return 1;
    string inputname = argv[1];
    string outputname = argv[2];


    FILE *inputfile = fopen(inputname.c_str(), "rb");
    
    BITMAPFILEHEADER bfh;
    BITMAPINFOHEADER bih;
    
    // reads the amount of bytes of a bfh and bih from input file into local program memory
    //fread where, how much, how often, input file
    fread(&bfh.bfType, 2, 1, inputfile);
    fread(&bfh.bfSize, 4, 1, inputfile);
    fread(&bfh.bfReserved1, 2, 1, inputfile);
    fread(&bfh.bfReserved2, 2, 1, inputfile);
    fread(&bfh.bfOffBits, 4, 1, inputfile);
    fread(&bih, sizeof(BITMAPINFOHEADER), 1, inputfile); // Fixed size structure, so it can be read in one operation
    
    int w = bih.biWidth;
    int h = bih.biHeight;
    int bytesPerPixel = bih.biBitCount / 8; // 3 BYTES, stored in BGR order
    int rowSize = ((w * bytesPerPixel + 3) / 4) * 4;
    int size = rowSize * abs(h);
    bih.biSizeImage = size;
    bfh.bfSize = bfh.bfOffBits + bih.biSizeImage;
    
    fseek(inputfile, bfh.bfOffBits, SEEK_SET);
    BYTE* data = (BYTE *)malloc(size);
    fread(data, size, 1, inputfile);
    fclose(inputfile);

    // ----- FORCE STANDARD BMP HEADER HERE -----
    bih.biSize = 40;
    bih.biSizeImage = size;
    bfh.bfOffBits = 54;
    bfh.bfSize = 54 + size;

    FILE *outfile = fopen(outputname.c_str(), "wb"); // creates a new file in write bytes mode
    BYTE* out = (BYTE *) malloc(size);

    fwrite(&bfh.bfType,      2, 1, outfile);
    fwrite(&bfh.bfSize,      4, 1, outfile);
    fwrite(&bfh.bfReserved1, 2, 1, outfile);
    fwrite(&bfh.bfReserved2, 2, 1, outfile);
    fwrite(&bfh.bfOffBits,   4, 1, outfile);
    fwrite(&bih, sizeof(BITMAPINFOHEADER), 1, outfile);

    for (int x = 0; x < w; x++)
    {
        for (int y = 0; y < h; y++)
        {
            int idx = y * rowSize + x * 3;

            PIXEL p;
            BYTE B = data[idx];
            BYTE G = data[idx + 1];
            BYTE R = data[idx + 2];
            p = { B, G, R };

            // keeps each pixel the same, making an exact copy in outfile.
            PIXEL o;
            o = { B, G, R };
            out[idx + 0] = B; 
            out[idx + 1] = G; 
            out[idx + 2] = R;
        }
    }
    
    fwrite(out, size, 1, outfile);
    fclose(outfile);
    return 0;

}