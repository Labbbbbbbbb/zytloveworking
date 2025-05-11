#include "head.h"

void Servo_Task(void *argument)
{
    osDelay(100);
    for (;;) {
//#ifdef 红绿都一样，伺服线程一样做，只是spe的来源不同
        
    if((mode2==0||mode1==0)&&Q_NO!=2)
   {
    WritePosEx(1, 2048, 1000, 50);
    WritePosEx(2, 2223, 1000, 50);
   }

   #ifdef RED  
   if((mode2==0||mode1==0)&&Q_NO!=2)
   {
    WritePosEx(1, tar_pos1, 1000, 50);
    WritePosEx(2, tar_pos2, 1000, 50);
   }
   #endif // 只用于红光题号2时
   

    if(mode2==1){
      WriteSpe(2,spe2,50);
    }
     if(mode1==1){
      WriteSpe(1,spe1,50);
    }
       // #endif 
        osDelay(1);
    }
        
    
}

void Servo_Start(void)
{
    osThreadId_t ServoHandle;
    const osThreadAttr_t Servo_attributes = {
        .name       = "Servo",
        .stack_size = 128 * 10,
        .priority   = (osPriority_t)osPriorityNormal,
    };
    ServoHandle = osThreadNew(Servo_Task, NULL, &Servo_attributes);
}
