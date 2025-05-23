#include "main.h"
#include "SCServo.h"

void FT_Write_Speed_Setup(void)
{
	setEnd(0);//SMS_STS舵机为大端存储结构
  WheelMode(1);//舵机ID1切换至电机恒速模式
}

void FT_Write_Speed(void)
{
  //舵机(ID1)以加速度A=50*8.7deg/s^2，加速至最高速度V=60*0.732=43.92rpm，并保持恒速正向旋转
  WriteSpe(1, 60, 50);
  HAL_Delay(5000);
  
  //舵机(ID1)以加速度A=50*8.7deg/s^2，减速至速度0停止旋转
  WriteSpe(1, 0, 50);
  HAL_Delay(2000);
  
  //舵机(ID1/ID2)以加速度A=50*8.7deg/s^2，加速至最高速度V=-60*0.732=-43.92rpm，并保持恒速反向旋转
  WriteSpe(1, -60, 50);
  HAL_Delay(5000);
  
  //舵机(ID1/ID2)以加速度A=50*8.7deg/s^2，减速至速度0停止旋转
  WriteSpe(1, 0, 50);
  HAL_Delay(2000);
}
