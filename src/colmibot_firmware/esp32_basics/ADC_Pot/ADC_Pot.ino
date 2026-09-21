#define POT 15 // Define el pin 15 del ESP32 para leer el potenciómetro

void setup() {
  Serial.begin(115200); // Inicia la comunicación serial a 115200 baudios
}

void loop() {
  int valor = analogRead(POT); // Lee el valor analógico (ADC) del potenciómetro
  Serial.println(valor);       // Envía el valor leído por el puerto serial
  delay(100);                  // Espera 100 ms antes de la siguiente lectura
}