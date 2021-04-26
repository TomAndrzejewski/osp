/* USER CODE BEGIN Includes */
#include "servo.h"
/* USER CODE END Includes */

/* USER CODE BEGIN PV */
uint8_t sign;
uint8_t message[20];
uint16_t message_length;
/* USER CODE END PV */

/* USER CODE BEGIN 2 */
HAL_UART_Receive_IT(&huart2, &sign, 1);
HAL_TIM_PWM_Start(&htim3,TIM_CHANNEL_4);
/* USER CODE END 2 */
  
/* USER CODE BEGIN 4 */
void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart)
{
	if(huart->Instance == USART2)
	{
		if(sign=='1')
		{
			int mode =1;
			message_length = sprintf(message, "Closed\n");
			set_ang(mode);
		}
		else
		{
			int mode =0;
			message_length = sprintf(message, "Open\n");
			set_ang(mode);
		}
		HAL_UART_Transmit_IT(&huart2, message, message_length);
		HAL_UART_Receive_IT(&huart2, &sign, 1);
	}
}
/* USER CODE END 4 */
