import java.io.*;
import java.util.*;
class Bikers
{
static float S1,S2,S3,S4,S5;
static float AvgSpeed;
public static void main(String args[ ])
{
Scanner input = new Scanner(System.in);
System.out.println(" Enter Speed of five Bike Racer");
S1 = input.nextInt();
S2 = input.nextInt();
S3 = input.nextInt();
S4 = input.nextInt();
S5 = input.nextInt();
AvgSpeed=(S1+S2+S2+S3+S4+S5)/5;
if( S1>AvgSpeed)
System.out.println("The Speed of Qualifying Racer is"+S1);
if( S2>AvgSpeed)
System.out.println(" The Speed of Qualifying Racer is"+S2);
if( S3>AvgSpeed)
System.out.println(" The Speed of Qualifying Racer is"+S3);
if( S4>AvgSpeed)
System.out.println(" The Speed of Qualifying Racer is"+S4);
if( S5>AvgSpeed)
System.out.println(" The Speed of Qualifying Racer is"+S5);
}
}