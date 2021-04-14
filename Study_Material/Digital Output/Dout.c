/*

TITLE	: Digital Output
DATE	: 2020/01/06
AUTHOR	: e-Yantra Team

AIM: To individually blink of the Red LED.

CONNECTIONS:
* Red Led 	-> PIN_LED_RED

NOTE:
* All the LEDs are Active Low.

*/

#define F_CPU 16000000UL		// Define Crystal Frequency of Uno Board
#include <avr/io.h>				// Standard AVR IO Library
#include <util/delay.h>			// Standard AVR Delay Library

#define PIN_LED_RED		PB5		// Macro for Pin Number of Red Led

void init_led(){
	DDRB    |= (1 << PIN_LED_RED);     // initialize the pins PIN_LED_RED of port B as output pins.
	PORTB   |= (1 << PIN_LED_RED);     // set the values that all the LEDs remains off initially
}


void led_redOff(void){
	PORTB &= ~(1 << PIN_LED_RED);		// Make PBPIN_LED_RED Low
}

void led_redOn(void){
	PORTB |= (1 << PIN_LED_RED);		// Make PBPIN_LED_RED High
}


int main(void){
	
	init_led();		// initialize led pins

	while(1){
		// turn ON red led for 1000 ms and OFF for 1000 ms
		led_redOn();
		_delay_ms(1000);
		led_redOff();
		_delay_ms(3000);
	}
	
}

