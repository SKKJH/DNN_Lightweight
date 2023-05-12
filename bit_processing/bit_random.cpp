#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <string.h>
#include <time.h>

void RemoveFirst(char *buf) {
    int i = 0;
    for (i = 1; buf[i]; i++)//buf[i]가 참(널문자가 아님)이면 반복하여라.
    {
        buf[i - 1] = buf[i]; //buf[i] 문자를 buf[i-1]로 이동
    }
    //현재 i는 널문자가 있는 위치, i-1은 마지막 문자 위치
    buf[i - 1] = '\0';
}

float bit_change(float x, int n) {
    int tmp = *reinterpret_cast<int*>(&x);
    int k = 32 - n;
    int mask = (1 << k) - 1;

    srand(time(NULL));
    int random_bits = rand() & mask; // Generate random n bits
    tmp &= ~mask; // Clear the last n bits of the float
    tmp |= random_bits; // Set the last n bits of the float to random values

    return *reinterpret_cast<float*>(&tmp);
}


// float bit_change(float x, int n) {
//     int tmp = *reinterpret_cast<int*>(&x);
//     int k = 32 - n;
//     int mask = (1 << k) - 1; // Create a mask with n bits set to 1
//     tmp |= mask; // Set the last n bits of the float to 1
//     return *reinterpret_cast<float*>(&tmp);
// }

// float bit_change(float x, int n) {
//     int tmp = *reinterpret_cast<int*>(&x);
//     int k = 32 - n;
//     tmp >>= k;
//     tmp <<= k;
//     return *reinterpret_cast<float*>(&tmp);
// }

void process_file(const char* input_path, const char* output_path, int bit) {
    FILE *read = fopen(input_path, "r");
    printf("file : %s\n",input_path);
    FILE *write = fopen(output_path, "w");
    printf("file : %s\n",output_path);

    float b, c;
    int first_value = 1;
    while (fscanf(read, "%f\n", &b) != EOF) {
        c = bit_change(b, bit);
        if (first_value) {
            fprintf(write, "%f", c);
            first_value = 0;
        } else {
            fprintf(write, "\n%f", c);
        }
    }

    fclose(read);
    fclose(write);
}

void process_directory(const char* folder_path, int bit) {
    DIR *dir;
    struct dirent *entry;
    // printf(folder_path);
    if ((dir = opendir(folder_path)) == NULL) {
        printf("Error opening directory\n");
        exit(1);
    }

    char input_path[1024];
    char output_path[1024];
    char temp[1024];

    while ((entry = readdir(dir)) != NULL) {
        if (entry->d_type == DT_REG) {
            snprintf(input_path, sizeof(input_path), "%s/%s", folder_path, entry->d_name);
	    strncpy(temp, folder_path, 1024);
	    RemoveFirst(temp);
    	    strcpy(temp, "./shift");
            snprintf(output_path, sizeof(output_path), "%s/%s", temp, entry->d_name);
            process_file(input_path, output_path, bit);
        }
    }

    closedir(dir);
}
int main(int argc, char* argv[]) {
printf("\n1");
    int bit = atoi(argv[2]);
    //const char* folder_path = "./shift/saveorigin" + argv[1] + "only_txt";

    char folder_path[100];
    //strcpy(folder_path, "./shift/saveorigin_");
    strcpy(folder_path, "./saveorigin_");
    strcat(folder_path, argv[1]);
    strcat(folder_path, "_only_txt");
printf("\n1");
    
    process_directory(folder_path, bit);
printf("\n1");
    return 0;
}
