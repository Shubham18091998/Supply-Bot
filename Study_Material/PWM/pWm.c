/*
TITLE	: Analog Output using PWM
DATE	: 2019/11/12
AUTHOR	: e-Yantra Team

AIM: To decrease the brightness of Led and simultaneously increase the brightness of Led,
	 and repeat this cyclically, for this program a led needs to connected to PB3.
*/

#define F_CPU 16000000UL		// Define Crystal Frequency of Uno Board

#include <avr/io.h>				// Standard AVR IO Library
#include <util/delay.h>			// Standard AVR Delay Library
#include <avr/interrupt.h>		// Standard AVR Interrupt Library

#define PIN_LED_RED		PB3

void led_init(void){
	DDRB    |= (1 << PIN_LED_RED);    
	PORTB   |= (1 << PIN_LED_RED);    
}

// Timer 2 initialized in PWM mode for brightness control
// Prescale:64
// PWM 8bit fast, TOP=0x00FF
// Timer Frequency:225.000Hz
void timer2_init()
{
	cli(); //disable all interrupts
	
	TCCR2B = 0x00;	//Stop
	
	TCNT2 = 0xFF;	//Counter higher 8-bit value to which OCR2A value is compared with
	
	OCR2A = 0xFF;	//Output compare register low value for Led
	
	//  Clear OC2A, on compare match (set output to low level)
	TCCR2A |= (1 << COM2A1);
	TCCR2A &= ~(1 << COM2A0);

	// FAST PWM 8-bit Mode
	TCCR2A |= (1 << WGM20);
	TCCR2A |= (1 << WGM21);
	TCCR2B &= ~(1 << WGM22);
	
	// Set Prescalar to 64
	TCCR2B &= ~((1 << CS21) | (1 << CS20));
	TCCR2B |= (1 << CS22);
	
	sei(); //re-enable interrupts
}

// Function for brightness control of all LED
void brightness (unsigned char red_led){
	OCR2A = 255 - (unsigned char)red_led; 	// active low thats why subtracting by 255
}

//use this function to initialize all devices
void init_devices (void) {
	led_init();
	timer2_init();
}

//Main Function
int main(){
	init_devices();
	int step = 0;
	
	while(1){
		// decrease led brightness
		for (step = 0; step < 256; step++){			
			brightness(255 - step);
			_delay_ms(10);
			
		}
	}
}
