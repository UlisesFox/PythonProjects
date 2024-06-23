import java.util.Random;
/**
 *
 * @author Orhan Demirel
 */
public class Perceptron {

    double[] weights;
    double threshold;

    public void Train(double[][] inputs, int[] outputs, double threshold, double lrate, int epoch) {
        this.threshold = threshold;
        int n = inputs[0].length;
        int p = outputs.length;
        weights = new double[n];
        Random r = new Random();

        // Inicializar pesos
        for (int i = 0; i < n; i++) {
            weights[i] = r.nextDouble();
        }

        for (int i = 0; i < epoch; i++) {
            int totalError = 0;
            for (int j = 0; j < p; j++) {
                int output = Output(inputs[j]);
                int error = outputs[j] - output;

                totalError += error;

                for (int k = 0; k < n; k++) {
                    double delta = lrate * inputs[j][k] * error;
                    weights[k] += delta;
                }
            }
            System.out.println("Época " + (i + 1) + " - Error Total: " + totalError);
            if (totalError == 0)
                break;
        }
    }

    public int Output(double[] input) {
        double sum = 0.0;
        for (int i = 0; i < input.length; i++) {
            sum += weights[i] * input[i];
        }

        int resultado = sum > threshold ? 1 : 0;
        System.out.println("Entrada: " + java.util.Arrays.toString(input) + " Suma Ponderada: " + sum + " Salida: " + resultado);
        return resultado;
    }

    public static void main(String[] args) {
        Perceptron p = new Perceptron();
        double inputs[][] = { { 1, 1 }, { 0, 0 }, { 0, 0 }, { 1, 1 } };
        int outputs[] = { 0, 0, 0, 1 };

        p.Train(inputs, outputs, 0.2, 0.1, 200);
        System.out.println("Predicciones:");
        System.out.println("0 Y 0 = " + p.Output(new double[] { 0, 0 }));
        System.out.println("1 Y 0 = " + p.Output(new double[] { 1, 0 }));
        System.out.println("0 Y 1 = " + p.Output(new double[] { 0, 1 }));
        System.out.println("1 Y 1 = " + p.Output(new double[] { 1, 1 }));
    }
}
