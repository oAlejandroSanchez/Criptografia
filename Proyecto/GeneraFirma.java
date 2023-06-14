/*
 * Universidad Nacional Autónoma de México
 * Facultad de Ingeniería
 * 
 * Generación de las claves (pública y privada) y de la firma digital
*/

// Se importan las bibliotecas
import java.io.*;
import java.security.*;

// Clase general
public class GeneraFirma {
    public static void main(String[] args) {
        // Título
        System.out.println("\t\tCreando la firma digital...");

        if(args.length != 1) {
            System.out.println("Para ejecutar el programa se deben seguir los siguientes pasos: ");
            System.out.println("\t1) Se debe generar el archivo class --> 'javac GeneraFirma.java'");
            System.out.println("\t2) Se ejecuta el programa --> 'java GeneraFirma <archivo>'");
        } else try {
            // Se determina una clave privada
            KeyPairGenerator genClave = KeyPairGenerator.getInstance("RSA");

            // Se inicia el objeto genClave a través del método initialize, el cual tiene dos argumentos: 
            //     a. Tamaño de la clave es de 1024 bits.
            //     b. Fuente aleatorio.
            SecureRandom aleatorio = SecureRandom.getInstance("SHA1PRNG","SUN");
            genClave.initialize(1024, aleatorio);

            // Se genera el par de claves 
            // PrivateKey --> Clave privada
            // PublicKey --> Clave pública
            KeyPair pardeClaves = genClave.generateKeyPair();
            PrivateKey privada = pardeClaves.getPrivate();
            PublicKey publica = pardeClaves.getPublic();

            // Se crea la firma digital
            Signature firma = Signature.getInstance("MD5withRSA");
            firma.initSign(privada);

            // Se abre el archivo, guarda el contenido en un buffer y posteriormente se lo hace llegar 
            // al objeto firma
            FileInputStream archivo = new FileInputStream(args[0]);
            BufferedInputStream bufferIn = new BufferedInputStream(archivo);
            byte[] buffer = new byte[1024];
            int longitud;

            while(bufferIn.available() != 0) {
                longitud = bufferIn.read(buffer);
                firma.update(buffer, 0, longitud);
            }
            bufferIn.close();

            // Generando la firma digital de los datos
            byte[] firmaReal = firma.sign();

            // Se guardan los datos firmados en un archivo
            FileOutputStream archivoFirma = new FileOutputStream("firma.txt");
            archivoFirma.write(firmaReal);
            archivoFirma.close();
            System.out.println("Se ha creado el archivo 'firma.txt'");

            // Se guarda la clave pública en un archivo
            FileOutputStream clavePublica = new FileOutputStream("clavepublica.txt");
            clavePublica.write(publica.getEncoded());
            clavePublica.close();
            System.out.println("Se ha creado el archivo 'clavepublica.txt'");
        } catch(Exception error) {
            System.out.println("Hubo un error al ejecutar el programa: " + error);
        }
    }
}