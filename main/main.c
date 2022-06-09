#include <stdio.h>
#include <string.h>
#include <sys/fcntl.h>
#include <sys/errno.h>
#include <sys/unistd.h>
#include <sys/select.h>
#include "esp_log.h"
#include "esp_vfs.h"
#include "esp_vfs_dev.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "lora.h"
#include "driver/uart.h"

#define MAX_MSG_LENGTH 50
TaskHandle_t msgTx_handle;
const uart_port_t uart_num = UART_NUM_0;
static const char* TAG = "uart_select_example";
bool msgReady=false;

char msg[MAX_MSG_LENGTH]={0};

static void uart_select_task(void *arg)
{
   char str[MAX_MSG_LENGTH]= {0};
   uart_config_t uart_config = {
      .baud_rate = 115200,
      .data_bits = UART_DATA_8_BITS,
      .parity    = UART_PARITY_DISABLE,
      .stop_bits = UART_STOP_BITS_1,
      .flow_ctrl = UART_HW_FLOWCTRL_DISABLE,
      .source_clk = UART_SCLK_APB,
   };
   uart_driver_install(UART_NUM_0, 2*1024, 0, 0, NULL, 0);
   uart_param_config(UART_NUM_0, &uart_config);

   while (1) {
      int fd;
      if ((fd = open("/dev/uart/0", O_RDWR)) == -1) {
         ESP_LOGE(TAG, "Cannot open UART");
         vTaskDelay(5000 / portTICK_PERIOD_MS);
         continue;
      }
      // We have a driver now installed so set up the read/write functions to use driver also.
      esp_vfs_dev_uart_use_driver(0);
      ESP_LOGI(TAG,"STARTING:");
      while (1) {
         vTaskDelay(1);
         int s;
         fd_set rfds;
         struct timeval tv = {
               .tv_sec = 5,
               .tv_usec = 0,
         };
         FD_ZERO(&rfds);
         FD_SET(fd, &rfds);
         s = select(fd + 1, &rfds, NULL, NULL, &tv);
         vTaskDelay(1);
         if (s < 0) {
               ESP_LOGE(TAG, "Select failed: errno %d", errno);
               break;
         } else if (s == 0) {
               //ESP_LOGI(TAG, "Timeout has been reached and nothing has been received");
         } else {
               if (FD_ISSET(fd, &rfds)) {
                  char buf[2]={'a',0};//initializam un string de un caracter si string terminator
                  if (read(fd, &buf, 1) > 0) {
                     printf("%c",buf[0]);
                     fflush(stdout);
                     if(buf[0]==0x0A){
                        //copiem pana la MAX_MSG_LENGTH-1 de caractere 
                        //ca sa avem string terminator 
                        //pe pozitia MAX_MSG_LENGTH in cel mai rau caz
                        strncpy(msg,str,MAX_MSG_LENGTH-1);
                        printf("Message: %s\n",msg);
                        str[0]=0;//string terminator pe prima pozitie ,practic stergem string-ul
                        msgReady=true;
                        continue;
                     }
                     strncat(str,buf,1);
                  } else {
                     ESP_LOGE(TAG, "UART read error");
                     break;
                  }
               } else {
                  ESP_LOGE(TAG, "No FD has been set in select()");
                  break;
               }
         }
      }
      close(fd);
   }
   vTaskDelete(NULL);
}

void task_contTx(void *p)
{
   char message[5] = "N";
   char msgASCIIcode[3]="0";
   uint8_t msgCount=0;
   for(;;) {
      vTaskDelay(pdMS_TO_TICKS(10000)); 
      //vTaskDelay(1);
      itoa(msgCount,msgASCIIcode,10);
      strcpy(message,"N");
      strcat(message,msgASCIIcode);
      msgCount++;
      lora_send_packet((uint8_t*) message, sizeof(message));
      printf("packet sent: %s\n",message);
   }
}

void task_msgTx(void *p){
   int length = 0;
   for(;;){
      if(msgReady){
         length=strlen(msg);
         if(length>MAX_MSG_LENGTH) length=MAX_MSG_LENGTH;
         lora_send_packet((uint8_t*) msg,length);
         printf("packet sent: %s\n",msg);
         msgReady=false;
      }
      vTaskDelay(5);
   }
   vTaskDelete(msgTx_handle);
}

void app_main()
{
   lora_init();
   lora_set_bandwidth(125E3);
   lora_set_frequency(8683e5);
   lora_enable_crc();
   lora_set_tx_power(2);
   //xTaskCreate(&task_contTx,"task_contTx",2048,NULL,6,NULL);
   xTaskCreate(&task_msgTx,"task_msgTx",2048,NULL,5,&msgTx_handle);
   xTaskCreate(&uart_select_task,"uart_select_task",2048,NULL,4,NULL);
}