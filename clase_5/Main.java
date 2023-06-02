import java.util.Random;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.concurrent.atomic.AtomicInteger;

public class Main {
    static AtomicInteger dato = new AtomicInteger(0);
    static AtomicBoolean leido = new AtomicBoolean(false);
    static AtomicInteger contador = new AtomicInteger(0);

    public static void main(String[] args) {
        System.out.println("Inicio programa principal");
        System.out.println("Valor Inicial: " + dato);

        Thread procesador1 = new Thread(new Procesador());
        Thread procesador2 = new Thread(new Procesador());
        Thread generador1 = new Thread(new Generador());

        procesador1.start();
        procesador2.start();
        generador1.start();
    }

    static class Procesador implements Runnable {
        @Override
        public void run() {
            Random rand = new Random();
            while (true) {
                System.out.println(Thread.currentThread().getName() + " Se proceso el dato : " + dato);
                contador.incrementAndGet();
                if (!leido.get()) {
                    leido.set(true);
                }
                try {
                    Thread.sleep(rand.nextInt(5000) + 1);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    static class Generador implements Runnable {
        @Override
        public void run() {
            Random rand = new Random();
            while (true) {
                if (leido.get() && contador.get() >= 2) {
                    leido.set(false);
                    dato.set(rand.nextInt(101));
                    contador.set(0);
                    System.out.println("Se genero un nuevo dato = " + dato);
                }
                try {
                    Thread.sleep(rand.nextInt(5000) + 1);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}