#define PIN_X 32 // Pin analógico para el eje X
#define PIN_Y 33 // Pin analógico para el eje Y

void setup() {
  Serial.begin(115200); // Inicializa comunicación serial
}

void loop() {
  int val_x = analogRead(PIN_X); // Lee voltaje eje X (0 a 4095)
  int val_y = analogRead(PIN_Y); // Lee voltaje eje Y (0 a 4095)
  
  Serial.print(val_x); // Imprime X
  Serial.print(",");   // Imprime separador
  Serial.println(val_y); // Imprime Y y salta de línea
  delay(50); // Pausa de 50ms para estabilidad
}