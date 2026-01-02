#include <cstdio>
#include <cstdint>
#include <cstring>

#pragma pack(push, 1)
struct BITMAPFILEHEADER {
    uint16_t bfType = 0x4D42; // 'BM'
    uint32_t bfSize;
    uint16_t bfReserved1 = 0;
    uint16_t bfReserved2 = 0;
    uint32_t bfOffBits = 54; // 14 + 40
};

struct BITMAPINFOHEADER {
    uint32_t biSize = 40;
    int32_t  biWidth = 3;
    int32_t  biHeight = 3;
    uint16_t biPlanes = 1;
    uint16_t biBitCount = 24;
    uint32_t biCompression = 0; // BI_RGB
    uint32_t biSizeImage;
    int32_t  biXPelsPerMeter = 0;
    int32_t  biYPelsPerMeter = 0;
    uint32_t biClrUsed = 0;
    uint32_t biClrImportant = 0;
};
#pragma pack(pop)

int main() {
    FILE* f = fopen("custom_made.bmp", "wb");

    const int width = 3;
    const int height = 3;
    const int bytesPerPixel = 3;
    const int rowSize = ((width * bytesPerPixel + 3) / 4) * 4;
    const int imageSize = rowSize * height;

    BITMAPFILEHEADER bfh;
    BITMAPINFOHEADER bih;

    bih.biSizeImage = imageSize;
    bfh.bfSize = bfh.bfOffBits + imageSize;

    fwrite(&bfh, sizeof(bfh), 1, f);
    fwrite(&bih, sizeof(bih), 1, f);

    unsigned char row[rowSize];
    memset(row, 0, rowSize); // padding bytes = 0

    // ---- ROW 3 (bottom): Black, Black, Green ----
    row[0] = 0;   row[1] = 0;   row[2] = 0;     // Black
    row[3] = 0;   row[4] = 0;   row[5] = 0;     // Black
    row[6] = 0;   row[7] = 255; row[8] = 0;     // Green
    fwrite(row, rowSize, 1, f);

    // ---- ROW 2: Black, Blue, White ----
    row[0] = 0;   row[1] = 0;   row[2] = 0;     // Black
    row[3] = 255; row[4] = 0;   row[5] = 0;     // Blue
    row[6] = 255; row[7] = 255; row[8] = 255;   // White
    fwrite(row, rowSize, 1, f);

    // ---- ROW 1 (top): Red, White, White ----
    row[0] = 0;   row[1] = 0;   row[2] = 255;   // Red
    row[3] = 255; row[4] = 255; row[5] = 255;   // White
    row[6] = 255; row[7] = 255; row[8] = 255;   // White
    fwrite(row, rowSize, 1, f);

    fclose(f);
    return 0;
}
