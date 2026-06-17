public class ExemploDoWhile {
    public static void main(String[] args) {
        int contador = 1;  // Inicializa o contador com 1

        do {
            System.out.println("Contador está em " + contador);  // Imprime o valor atual do contador
            contador++;  // Incrementa contador em 1
        } while (contador <= 5);  // Continua o loop enquanto contador for menor ou igual a 5
    }
}