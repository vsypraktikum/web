#include<wiringPi.h>
#include<signal.h>
#include<stdio.h>
#include<pthreahd.h>
#include<semaphre.h>

int status;
double distanz,
sem_t S_Messung, S_Anzeige, S_Bewegung;
double differenz;

void *Bewegung()
{
while (1) {
status = digitalRead (13);

	if(status == 1){
		
		sem_post (&S_Messung);  //V-Operation

		sem_wait(&S_Bewegung);  //P-Operation
			}
	 }
}

void *Entfernung(){
unsigned int t1,t2;

while(1){
sem_wait(&S_Messung); // P-Operation

	if(status =1){
		digitalWrite(6,1);
		delay(0.01);
		digitalWrite(6,0);
		while(digitalRead(5) == 0){
			t1=micros();
			}
		while(digitalRead(5) ==1){
		t2 = micros();
			}
		differenz = (double) (t2 - t1);
		differenz = differenz / 1000000
		distanz = (differenz*34000)/2;
		printf("Distanz: %lf\n",distanz);
			}
sem_post(&S_Anzeige); // V-Operation
     }
}

void *Anzeige(){
while(1){
	sem_wait(&S_Anzeige); // P-Operation
	digitalWrite(17,0);
	digitalWrite(18,0);
	digitalWrite(27,0);
		if(distanz<15){
			digitalWrite(17,1);
			}
		else if(distanz >15 && distanz < 30){
			digitalWrite(18,1);
				}
		else if(distanz > 30){
			digitalWrite(27,1);
			}
sem_post(&S_Bewegung); // V-Operation

  }
}


int main(void){

wiringPiSetupGpio();
pinMode(17, OUTPUT); //rot
pinMode(18, OUTPUT); //gelb
pinMode(27, OUTPUT); // grün
pinMode(6, OUTPUT); // trig
pinMode(5, OUTPUT); //echo
pinMode(13, OUTPUT); // bewegung

pthread_t thread1, thread2, thread3;

sem_init(&S_Bewegung,0,0);
sem_init(&S_Messung,0,0);
sem_init(&S_Anzeige,0,0);


delay(15000);

pthread_kill(thread1,  9);  //9 = SIGKILL
pthread_kill(thread2, 9);
pthread_kill(thread3,  9);

return 0;

}










