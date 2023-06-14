/* 
 * Universidad Nacional Autónoma de México
 * Facultad de Ingeniería
 * 
 * Se realiza la verificación de la firma digital
*/

// Se importan las bibliotecas
import java.io.*;
import java.security.*;
import java.security.spec.*;

public class VerificaFirma {
    public static void main(String[] args) {
        System.out.println("\t\tVerificación de la firma digital...");

        if(args.length != 3) {
            System.out.println("Para ejecutar el programa se deben seguir los siguientes pasos: ");
            System.out.println("\t1) Se debe generar el archivo class --> 'javac VerificaFirma.java'");
            System.out.println("\t2) Se ejecuta el programa --> 'java VerificaFirma clavepublica.txt datosaFirmar.txt'");
        } else try {
            // Se importan los bytes codificados de la clave pública del archivo que lo contiene y
            // y los convierte en un objeto de tipo PublicKey
            FileInputStream clavePublica = new FileInputStream(args[0]);
            byte[] clave = new byte[clavePublica.available()];
            clavePublica.read(clave);
            clavePublica.close();

            // Se obtiene el valor de la clave pública
            X509EncodedKeySpec publicKeySpec = new X509EncodedKeySpec(clave);
            
            // Se requiere para realizar la conversión
            KeyFactory keyFactory = KeyFactory.getInstance("RSA");

            // Se genera un objeto PublicKey
            PublicKey clvPublica = keyFactory.generatePublic(publicKeySpec);

            // Se introducen los bytes firmados desde el archivo especificado
            FileInputStream archivoFirmado = new FileInputStream(args[1]);
            byte[] firmaVerificada = new byte[archivoFirmado.available()];
            archivoFirmado.read(firmaVerificada);
            archivoFirmado.close();

            // Se define los algoritmos usados en este proceso
            Signature firma = Signature.getInstance("MD5withRSA");
            firma.initVerify(clvPublica);

            // Se suministran los datos para los cuales se generó la lista
            FileInputStream datos = new FileInputStream(args[2]);
            BufferedInputStream bufferIn = new BufferedInputStream(datos);
            byte[] buffer = new byte[1024];
            int longitud;

            while(bufferIn.available() != 0) {
                longitud = bufferIn.read(buffer);
                firma.update(buffer, 0, longitud);
            }
            bufferIn.close();

            // Se reporta el resultado
            boolean verifica = firma.verify(firmaVerificada);
            System.out.println("\tVerificación de la firma: " + verifica);

        } catch(Exception error) {
            System.err.println("Hubo un error en la verificación: " + error);
        }
    }
}
