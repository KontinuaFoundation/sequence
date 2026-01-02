#include <cstdio>
#include <cstdint>
#include <cstring>


#pragma pack(push, 1)
struct BITMAPFILEHEADER {
    uint16_t bfType = 0x4D42; // 'BM'
    uint32_t bfSize;
    uint16_t bfReserved1 = 0;
    uint16_t bfReserved2 = 0;
    uint32_t bfOffBits = 54;
};

struct BITMAPINFOHEADER {
    uint32_t biSize = 40;
    int32_t  biWidth = 4;
    int32_t  biHeight = 2;
    uint16_t biPlanes = 1;
    uint16_t biBitCount = 24;
    uint32_t biCompression = 0;
    uint32_t biSizeImage;
    int32_t  biXPelsPerMeter = 0;
    int32_t  biYPelsPerMeter = 0;
    uint32_t biClrUsed = 0;
    uint32_t biClrImportant = 0;
};
#pragma pack(pop)

int main(int argc, char const *argv[])
{
    FILE* f = fopen("fourbytwo.bmp", "wb");
    
    BITMAPFILEHEADER bfh;
    BITMAPINFOHEADER bih;
    
    const int width = 4;
    const int height = 2;
    const int bytesPerPixel = 3;
    const int rowSize = ((width * bytesPerPixel + 3) / 4) * 4; // 12
    const int imageSize = rowSize * height;                    // 24
    
    bih.biSizeImage = imageSize;
    bfh.bfSize = bfh.bfOffBits + imageSize;
    
    fwrite(&bfh, sizeof(bfh), 1, f);
    fwrite(&bih, sizeof(bih), 1, f);
    uint8_t row[rowSize];

    // ----------------------------
    // Write bottom row first:
    // [ Black ] [ Red ] [ Green ] [ Blue ]
    // ----------------------------
    std::memset(row, 0, rowSize);

    // Black
    row[0] = 0;   row[1] = 0;   row[2] = 0;
    // Red (BGR = 0,0,255)
    row[3] = 0;   row[4] = 0;   row[5] = 255;
    // Green (BGR = 0,255,0)
    row[6] = 0;   row[7] = 255; row[8] = 0;
    // Blue (BGR = 255,0,0)
    row[9] = 255; row[10]= 0;   row[11]= 0;

    fwrite(row, rowSize, 1, f);

    // ----------------------------
    // Write top row:
    // [ Yellow ] [ Magenta ] [ Cyan ] [ White ]
    // ----------------------------
    std::memset(row, 0, rowSize);

    // Yellow (BGR = 0,255,255)
    row[0] = 0;   row[1] = 255; row[2] = 255;
    // Magenta (BGR = 255,0,255)
    row[3] = 255; row[4] = 0;   row[5] = 255;
    // Cyan (BGR = 255,255,0)
    row[6] = 255; row[7] = 255; row[8] = 0;
    // White (BGR = 255,255,255)
    row[9] = 255; row[10]= 255; row[11]= 255;

    fwrite(row, rowSize, 1, f);

    fclose(f);
    return 0;
}
