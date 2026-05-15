
#define ledPin1 2
#define ledPin2 3
#define ledPin3 4
#define ledPin4 5

#define btnPin1 6
#define btnPin2 7

bool systemOn = false;
int currentMode = 1;

bool lastbtn1State = LOW;
bool lastbtn2State = LOW;

void setup() {

  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin3, OUTPUT);
  pinMode(ledPin4, OUTPUT);

  pinMode(btnPin1, INPUT);
  pinMode(btnPin2, INPUT);
}

void loop() {
  
  bool btn1State = digitalRead(btnPin1);
  bool btn2State = digitalRead(btnPin2);

  // Buton 1; aç kapa
  if (btn1State == HIGH && lastbtn1State == LOW) {
    systemOn = !systemOn; 
    if (!systemOn) {
      allOff();
    }
    delay(50);
  }
  lastbtn1State = btn1State;

  // Buton 2; Mod Değiştirme
  if (systemOn && btn2State == HIGH && lastbtn2State == LOW) {
    currentMode++;
    if (currentMode > 3) {
      currentMode = 1;
    }
    delay(50);
  }
  lastbtn2State = btn2State;

  if (systemOn) {
    if (currentMode == 1) {
      mode1();
    } else if (currentMode == 2) {
      mode2();
    } else if (currentMode == 3) {
      mode3();
    }
  }
}

// Modlar

void mode1() {
  digitalWrite(ledPin1, HIGH); digitalWrite(ledPin2, HIGH);
  digitalWrite(ledPin3, HIGH); digitalWrite(ledPin4, HIGH);
  delay(1000);
  allOff();
  delay(1000);
}

void mode2() {
  int leds[] = {ledPin1, ledPin2, ledPin3, ledPin4};
  for (int i = 0; i < 4; i++) {
    if (!digitalRead(btnPin1)) { 
      allOff();
      digitalWrite(leds[i], HIGH);
      delay(1000);
    }
  }
}

void mode3() {
  int leds[] = {ledPin1, ledPin2, ledPin3, ledPin4};
  for (int i = 3; i >= 0; i--) {
    allOff();
    digitalWrite(leds[i], HIGH);
    delay(1000); 
  }
}

void allOff() {
  digitalWrite(ledPin1, LOW);
  digitalWrite(ledPin2, LOW);
  digitalWrite(ledPin3, LOW);
  digitalWrite(ledPin4, LOW);
}