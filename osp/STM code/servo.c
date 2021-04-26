/*
 * servo.c
 *
 *  Created on: Mar 18, 2021
 *      Author: Tomasz Budzynski, Adam Sankowski
 */
#include "servo.h"
#include "tim.h"



void set_ang(uint8_t mode)
{
	uint16_t val;
	uint16_t MIN=1000;
	uint16_t MAX=1550;
	if(mode==1)
	{
	 val=MAX;
	}
	else if(mode==0)
	{
	val=MIN;
	}

	__HAL_TIM_SET_COMPARE(&htim3,TIM_CHANNEL_4,val);
}


