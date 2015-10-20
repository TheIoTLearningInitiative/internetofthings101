/*
 * mBotBluetooth.ino
 *
 * Enable direction commands via Bluetooth
 *
 * Authored by: Yonattan Louise,  Javier Perez, Gerardo Acevedo
 *
 */

#include <Arduino.h>
#include <Wire.h>
#include <Servo.h>
#include <SoftwareSerial.h>

#include <MeMCore.h>

double angle_rad = PI/180.0;
double angle_deg = 180.0/PI;

MeDCMotor motor_9(9);
MeDCMotor motor_10(10);
MeBuzzer buzzer;
MeBluetooth bluetooth(PORT_4);

void setup()
{
  Serial.begin(115200);
  bluetooth.begin(115200);
}

void loop()
{
  // Bluetooth comunication
  if (Serial.available())
  {
    char cmd_id;
    int value;
    String command = Serial.readString();
    String answer;
    char cmd_buf[100];
    if (command.length() > 0) {
      if (process_command(command)) {
        answer = String("OK");
      }
      else {
        answer = String("Error");
      }
      sprintf(cmd_buf, "%s", answer.c_str());
      Serial.write(cmd_buf);
      command = "";
    }
  }
}

int command_decode(String &command, char *pcmd_id, int *pvalue, int *pidnode)
{
  int index;
  
  *pcmd_id = 'b';
  *pvalue = 250;
  
  index = command.indexOf("=");
  if (index != 1) {
    return 0;
  }

  *pcmd_id = command.charAt(0);
  index = command.indexOf("/");
  if (index > 0) {
    *pvalue = command.substring(2, index).toInt();
  }

  *pidnode = 0;
  int index_command = index;
  index = command.indexOf(";");
  if (index > 0) {
    *pidnode = command.substring(index_command+1, index).toInt();
  }
  
  return 1;
}

int move_motor(int mL, int mR, int t)
{
    motor_9.run((9)==M1?-(mL):(mL));
    motor_10.run((10)==M1?-(mR):(mR));
    delay(t);
    motor_9.run((9)==M1?-(0):(0));
    motor_10.run((10)==M1?-(0):(0));
}

int identify(int id_node) {
  if ((id_node > 9) || (id_node < 0)) {
    return 0;
  }
  
  for(int i=0; i<id_node; i++){
    buzzer.tone(6000, 30);
    delay(500);
  }
}

int process_command(String command)
{
  char cmd_id;
  int value;
  int id_note;
  
  if (command.length() > 0) {
    if (!command_decode(command, &cmd_id, &value, &id_note)) {
      return 0;
    }
    identify(id_note);
    switch (cmd_id) {
      case 'f':
      case 'F':
        move_motor(255, 255, value);
        break;
      case 'b':
      case 'B':
        move_motor(-255, -255, value);
        break;
      case 'l':
      case 'L':
        move_motor(-255, 255, value);
        break;
      case 'r':
      case 'R':
        move_motor(255, -255, value);
        break;
      default:
        return 0;
    }
    return 1;
  }
  return 0;
}

