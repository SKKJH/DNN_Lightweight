#include <string.h>
#include <stdio.h>
#include <stdlib.h>

float bit_change(float x, int n){

	int tmp;
	memcpy(&tmp, &x, sizeof tmp);
	int k = 32 - n;
	tmp >>= k;
	tmp <<= k;
	float result;
	memcpy(&result, &tmp, sizeof result);

	return result;
}

int main(){
	
char line[10000];
char* p;
float c;
float b;
	FILE* read = fopen("beta.txt", "r");
	FILE* write = fopen("shiftbeta.txt", "w");
	while (fgets(line, sizeof(line), read) != NULL ) {

		//printf("%s", line);
		p = strtok(line, ",");
		int flag = 0;
    		while(p != NULL){
	        	if (flag != 0){
				fputs(",",write); 
			}
        		b = atof(p);
        		c = bit_change(b,30);
			fprintf(write, "%f", c);
			p=strtok(NULL, ",");
			flag += 1;
    		}
	fputs("\n",write); 
	}

	fclose(read);
	fclose(write);

	return 0;
}



