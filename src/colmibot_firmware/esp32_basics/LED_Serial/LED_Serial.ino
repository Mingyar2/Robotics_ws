#define LED 2 // Define el pin 2 del ESP32 para el LED integrado

void setup() {
  pinMode(LED, OUTPUT); // Configura el pin del LED como salida
  Serial.begin(115200); // Inicia la comunicación serial a 115200 baudios
}

void loop() {
  if (Serial.available() > 0) { // Verifica si hay datos llegando por el puerto serial
    char dato = Serial.read();  // Lee el carácter entrante

    if (dato == '1') {
      digitalWrite(LED, HIGH);  // Si el dato recibido es '1', enciende el LED
    }
    if (dato == '0') {
      digitalWrite(LED, LOW);   // Si el dato recibido es '0', apaga el LED
    }
  }
}
