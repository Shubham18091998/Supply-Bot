/*
TITLE	: Digital Input
DATE	: 2019/11/12
AUTHOR	: e-Yantra Team

AIM	: To turn on the green led when onboard user button is pressed otherwise turn it off.

CONNECTIONS:
* User Button 	-> PD5
* Red Led 	-> PB5

*/

#define F_CPU 16000000UL		// Define Crystal Frequency of Uno Board
#include <avr/io.h>				// Standard AVR IO Library
#include <util/delay.h> 			// Standard AVR Delay Library

#define PIN_LED_RED	PB5	// Macro for Pin Number of Green Led
#define PIN_BUTTON	PD5	// Macro for Pin Number of User Button 

void init_button(void){
	DDRD &= ~(1 << PIN_BUTTON);		// Make PIN_BUTTON input
	PORTD |= (1 << PIN_BUTTON);		// Turn on Internal Pull-Up resistor of PIN_BUTTON (Optional)
}

unsigned char button_read(void){
	unsigned char status = PIND >> PIN_BUTTON;	// Read PIN_BUTTON
	return status;
}

void init_led(void){
	DDRB    |= (1 << PIN_LED_RED);    // Make PIN_LED_GREEN Output
	PORTB   |= (1 << PIN_LED_RED);    // Clear PIN_LED_GREEN
}

void led_greenOn(void){
	PORTB &= ~(1 << PIN_LED_RED); 	// Clear PIN_LED_GREEN
}

void led_greenOff(void){
	PORTB |= (1 << PIN_LED_RED);		// Set PIN_LED_GREEN
}


int main(void){
	
	// initialize led and button
	init_led();
	init_button();

	while(1){

		// If button is pressed turn on the green led else turn it off
		if(button_read() == 1){
			led_greenOff();
		} else {
			led_greenOn();
		}
		
	}
	
}

