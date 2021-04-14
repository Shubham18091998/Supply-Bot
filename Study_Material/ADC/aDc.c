/*
TITLE	: Analog Input using ADC
DATE	: 2019/11/12
AUTHOR	: e-Yantra Team

AIM: Touch PC1 pin to turn the led else it should stay off, for this program a led needs to connected to PB3.
*/

#define F_CPU 16000000UL		// Define Crystal Frequency of Uno Board

#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>


#define PIN_ADC			PC1
#define PIN_LED_RED		PB3

unsigned char ADC_Value;
unsigned char adc_reading;
unsigned int value;


//ADC pin configuration
/*

1) Set all ADC Pins as Input.
2) Make all ADC Pins Floating

NOTE: if ADC pins are pulled-up then 5V will be on the pins. So, ADC wont give proper value.

*/
void adc_pin_config (void){
	DDRC &= ~(1 << PIN_ADC); //set PORTC direction as input
	PORTC &= ~(1 << PIN_ADC); //set PORTC pins floating
}

//Function to Initialize ADC
/*

1) Disable Analog Comparator
2) Turn ON ADC
3) Set Prescalar to 64

*/
void adc_init(){	
	ACSR = (1 << ACD);   	// Analog Comparator Disable; else ADC wont work	
	ADMUX = (1 << ADLAR);
	// (turn ADC ON) | (set prescalar to 64 110)
	ADCSRA = ((1 << ADEN) |  (1 << ADPS2 | 1 << ADPS1)) ;
}

//This Function accepts the Channel Number and returns the corresponding Analog Value
/* This function is for  Single Ended Channels Only */
unsigned char ADC_Conversion(unsigned char Ch)
{
	unsigned char a;	
	// Extract Last 3 bits from Ch for ADMUX
	Ch = Ch & 0b00000111; //0x07
	ADMUX = 0x20 | Ch; // (Left Adjusted Output) | (ADMUX4:0)
	//-----------------------------------------------------------------
	
	// ADMUX |= Ch;	// *** does not work if ADLAR is set in adc_init()
	//-----------------------------------------------------------------
	//-----------------------------------------------------------------
	ADCSRA |= (1 << ADSC);		//Set start conversion bit	
	// Wait for ADC conversion to complete; ADIF = 0, conversion going on; ADIF = 1, conversion complete
	while((ADCSRA & (1 << ADIF) ) == 0);	
	// store ADC value in variable are return it.
	a = ADCH;
	//-----------------------------------------------------------------
	//-----------------------------------------------------------------
	// ADIF is set when ADC conversion is complete and Data Registers are updated
	// ADIF needs to be cleared before starting next conversion
	ADCSRA |= (1 << ADIF); // IMP: clear ADIF (ADC Interrupt Flag) by writing 1 to it	
	//-----------------------------------------------------------------
	return a;
}


//Function to Initialize PORTS
void port_init()
{
	adc_pin_config();
}

void led_init(void){
	DDRB    |= (1 << PIN_LED_RED);
	PORTB   |= (1 << PIN_LED_RED);
}

// Timer 4 initialized in PWM mode for brightness control
// Prescale:256
// PWM 8bit fast, TOP=0x00FF
// Timer Frequency:225.000Hz
void timer2_init()
{
	cli(); //disable all interrupts	
	TCCR2B = 0x00;	//Stop	
	TCNT2 = 0xFF;	//Counter higher 8-bit value to which OCR5xH value is compared with
	//TCNT4L = 0x00;	//Counter lower 8-bit value to which OCR5xH value is compared with	
	//OCR4AH = 0x00;	//Output compare register high value for Red Led
	OCR2A = 0xFF;	//Output compare register low value for Red Led	
	//  Clear OC4A, OC4B & OC4C on compare match (set output to low level)
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

// Function for brightness control
void brightness (unsigned char red_led){
	OCR2A = 255 - (unsigned char)red_led; 	// active low thats why subtracting by 255
}

void init_devices (void)
{
	port_init();
	adc_init();
	led_init();
	timer2_init();
}

//Main Function
int main(void)
{
	unsigned int value;
	init_devices();
	
	while(1)
	{
		ADC_Value = ADC_Conversion(1);
		brightness(255 - ADC_Value);
	}
	
	return 0;
}