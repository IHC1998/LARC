//PINOS SENSOR DE COR
int S2 = 9;   //9   //2
int S3 = 10;   //10  //4
int OUT = 8;  //8   //7
int red;
int green;
int blue;

void color() {
  // ----- OBS: Os valores dessa tabela irão variar dependendo da luminosidade do local. ------
  /* Tabela de Valores do RGB das Cores
         COR  | RED | GREEN | BLUE |
       PRETO  | 13  |   22  |  20  |
     VERMELHO | 06  |   14  |  12  |
       VERDE  | 11  |   16  |  15  |
        AZUL  | 12  |   18  |  13  |
       CINZA  | 06  |   08  |  07  |
       BRANCO | 04  |   04  |  04  |
  */

  if (red < 11) {
    Serial.println("R");
}

  else if (11 < red && red < 25 && green < 20) {
    Serial.println("B");
  }

  else if (20 < red) {
    Serial.println("G");
  }
}

void calculo_RGB() {
  //Seleciona leitura com filtro para vermelho de acordo com a tabela lembra?
  digitalWrite(S2, LOW);
  digitalWrite(S3, LOW);
  //Lê duração do pulso em LOW
  red = pulseIn(OUT, LOW);  // Função que retorna a duração do pulso em ms

  //Seleciona leitura com filtro para verde
  digitalWrite(S2, HIGH);
  digitalWrite(S3, HIGH);
  //Lê duração do pulso em LOW
  green = pulseIn(OUT, LOW);

  //Seleciona leitura com filtro para azul
  digitalWrite(S2, LOW);
  digitalWrite(S3, HIGH);
  //Lê duração do pulso em LOW
  blue = pulseIn(OUT, LOW);

  color();
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(S2, OUTPUT);
  pinMode(S3, OUTPUT);
  pinMode(OUT, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  calculo_RGB();
}
