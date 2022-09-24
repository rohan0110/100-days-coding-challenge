public class quadratic {
    public static void main(String[] args) {
        int a,b,c;
        double d,x1,x2;
        a=1;
        b=0;
        c=-9;
        d=(b*b)-(4*a*c);
        if(d<0){
            System.out.println("roots are imaginary");
        }
        else{
            x1 = (-b + Math.sqrt (d)) / 2*a;
            x2 = (-b - Math.sqrt (d))/2*a;
            System.out.println("Root1 : "+x1);
            System.out.println("\nRoot2 : "+x2);
        }
    }
}
