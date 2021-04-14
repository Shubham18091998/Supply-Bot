

/*

TITLE	: Line Follower
DATE	: 2020/01/06
AUTHOR	: eYRC-2728


NOTE:
* All the LEDs are Active Low.

*/

#define F_CPU 16000000UL		// Define Crystal Frequency of Uno Board
#include <avr/io.h>				// Standard AVR IO Library
#include <util/delay.h>			// Standard AVR Delay Library
#include <avr/interrupt.h>		// Standard AVR Interrupt Library
#include "D:\Project Work\E-Yantra\Study Material\UART\uart.h"
#include "D:\Project Work\E-Yantra\Study Material\UART\uart.c"


//#############################################################################################################################
//UART MACROS
#define USART0_ENABLED
//#############################################################################################################################
//MOTOR MACROS
#define MOTOR1_IN_1 7
#define MOTOR1_IN_2 0
#define MOTOR2_IN_1 1
#define MOTOR2_IN_2 2
#define MOTOR_ENA 3
#define MOTOR_ENB 3
//##############################################################################################################################
//IR MACROS
#define IR_1 4
#define IR_2 5
#define IR_3 6
#define p1 ((PIND&(1<<IR_1))>>IR_1)
#define p2 ((PIND&(1<<IR_2))>>IR_2)
#define p3 ((PIND&(1<<IR_3))>>IR_3)
//#################################################################################################################################
//INITIALIZE IR
void init_ir(){
	DDRD&=~(1<<IR_1);     
	DDRD&=~(1<<IR_2);
	DDRD&=~(1<<IR_3);
	PORTD&=~(1<<IR_1);
	PORTD&=~(1<<IR_2);
	PORTD&=~(1<<IR_3);
}

//######################################################################################################################################
//INITIALIZE TIMER2
void timer2_init()
{
	cli();
	TCCR2A=(1<<COM2A1) | (1<<COM2A0) | (1<<COM2B1) | (1<<COM2B0) | (1<<WGM21) | (1<<WGM20);
	TCCR2B=(0<<WGM22) | (0<<CS22) | (0<<CS21) | (1<<CS20);
	TCNT2=0xFF;
	OCR2A=0x55;
	OCR2B=0x55;
	return;
	sei();
}

//########################################################################################################################################
//INITIALIZE MOTORS
void init_motor()
{
	DDRD|=(1<<MOTOR1_IN_1);
	DDRB|=(1<<MOTOR1_IN_2);
	DDRB|=(1<<MOTOR2_IN_1);
	DDRB|=(1<<MOTOR2_IN_2);
	DDRD|=(1<<MOTOR_ENA);
	DDRB|=(1<<MOTOR_ENB);
	PORTD|=(1<<MOTOR_ENB);
	PORTB|=(1<<MOTOR_ENB);
}
//#########################################################################################################################################
//TO READ FROM XBEE
char uart0_readByte(void){

	uint16_t rx;
	uint8_t rx_status, rx_data;

	rx = uart0_getc();
	rx_status = (uint8_t)(rx >> 8);
	rx = rx << 8;
	rx_data = (uint8_t)(rx >> 8);

	if(rx_status == 0 && rx_data != 0){
		return rx_data;
	} else {
		return -1;
	}

}

//##########################################################################################################################################
//SET FORWARD DIRECTION
void SET_DIRF()
{
	PORTD|=(1<<MOTOR1_IN_1);PORTB&=~(1<<MOTOR1_IN_2);
	PORTB|=(1<<MOTOR2_IN_1);PORTB&=~(1<<MOTOR2_IN_2);
	return;		// receives direction form python
}
//SET BACKWARD DIRECTION
void SET_DIRB()
{
	PORTD&=~(1<<MOTOR1_IN_1);PORTB|=(1<<MOTOR1_IN_2);
	PORTB&=~(1<<MOTOR2_IN_1);PORTB|=(1<<MOTOR2_IN_2);
	return;		// receives direction form python
}
//TURN MOTOR 1 ON FOR FORWARD MOTION
void MOTOR1_ONF()
{
	PORTD|=(1<<MOTOR1_IN_1);PORTB&=~(1<<MOTOR1_IN_2);
}
//TURN MOTOR 2 ON FOR FORWARD MOTION
void MOTOR2_ONF()
{
	PORTB|=(1<<MOTOR2_IN_1);PORTB&=~(1<<MOTOR2_IN_2);
}
//TURN MOTOR 1 ON FOR BACKWARD MOTION
void MOTOR1_ONB()
{
	PORTD&=~(1<<MOTOR1_IN_1);PORTB|=(1<<MOTOR1_IN_2);
}
//TURN MOTOR 2 ON FOR BACKWARD MOTION
void MOTOR2_ONB()
{
	PORTB&=~(1<<MOTOR2_IN_1);PORTB|=(1<<MOTOR2_IN_2);
}
//TURN MOTOR 1 OFF
void MOTOR1_OFF()
{
	PORTD|=(1<<MOTOR1_IN_1);PORTB|=(1<<MOTOR1_IN_2);
}
//TURN MOTOR 1 OFF
void MOTOR2_OFF()
{
	PORTB|=(1<<MOTOR2_IN_1);PORTB|=(1<<MOTOR2_IN_2);
}
//CHANGE MOTOR 1 DIRECTION
void MOTOR1_CD()
{
	PORTD^=(1<<MOTOR1_IN_1);PORTB^=(1<<MOTOR1_IN_2);
	
}
//CHANGE MOTOR 2 DIRECTION
void MOTOR2_CD()
{
	PORTB^=(1<<MOTOR2_IN_1);PORTB^=(1<<MOTOR2_IN_2);
}
//START FORWARD MOTION
void move_for()
{
	SET_DIRF();
	while(uart0_readByte()!='S')
	{
		if(p3!=0)
		{
			if(p1==0)
			{
				MOTOR1_OFF();
				while(p3!=0) ;
				MOTOR1_ONF();
			}
			else if(p2==0)
			{
				MOTOR2_OFF();
				while(p3!=0) ;
				MOTOR2_ONF();
			}
		}
	}
	MOTOR2_OFF();MOTOR1_OFF();
}
//START BACKWARD MOTION
void move_back()
{
	SET_DIRB();
	while(uart0_readByte()!='S')
	{
		if(p3!=0)
		{
			
			if(p2==0)
			{
				MOTOR1_OFF();
				while(p3!=0) ;
				MOTOR1_ONB();
			}
		}
	}
	MOTOR2_OFF();MOTOR1_OFF();
}
void hit()
{
	DDRD|=(1<<5);
	PORTD|=(1<<5);
	_delay_ms(50);
	PORTD&=~(1<<5);
	return
}

//#########################################################################################################################################
int main(void){

//INITIALIZATIONS HERE
	init_ir();
	init_motor();
	timer2_init();
	uart0_init(UART_BAUD_SELECT(9600, F_CPU));
	uart0_flush();
	
	//init_led();
	//while(1)
	//{
	//move_for();
	//_delay_ms(50000);
	//move_back();
	//_delay_ms(50000);
	//}
	
	
	char ch=-1;
	while(1)
	{
		ch=uart0_readByte();
		switch(ch)
		{
			case 'F':
			move_for();
			break;
			case 'B':
			move_back();
			break;
			case 'H':
			_delay_ms(500);
			hit();
			break;
			case 'Z':
			//buzz here
			break;
			default:
			break;
		}
	}
}


	