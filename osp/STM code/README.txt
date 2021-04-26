---Put servo.c in "Your_STM_Project_Name"/Core/Src

---Put servo.h in "Your_STM_Project_Name"/Core/Inc

---Put parts of code written in main.c in your main.c file, remember about putting it in special places indicated by comments

---In CubeMX, set:
	- Tim3:
		Clock Source: Internal Clock, 
		Channel4: PWM Generation CH4, 
		Prescaler: 100, 
		Counter Mode: Up, 
		Counter Period: 19999, 
		Internal Clock Division: No Division,
		auto-reload preload: Enable,
	- USART2:
		Mode: Asynchronous
		Hardware Flow Control: Disable
		Baud Rate: 115200 Bits/s
		Word Length: 8 Bits (including Parity)
		Parity: None
		Stop Bits: 1
		Data Direction: Recieve and Transmit
		Over Sampling: 16 Samples

---Clock Configuration:
	

---Project Manager:
	- In "Code Generator" set "Generate peripheral initialization as a pair of'.c/.h' files per peripheral

---To connect Micro Servo 9g with STM:
		 connect VCC (5V), GND to STM or external source of energy
		 connect PWM servo input with Timer output on STM

