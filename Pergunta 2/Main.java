import java.util.*;

public class Main{
    public static boolean fibonacci(int num){
        int a,b,c;
        a=c=0;
        b=1;
        while(num>=c){
            if(num==c){
                return true;
            } 

            c=a+b;
            a=b;
            b=c;

        }
        return false;
    }
    public static void main(String[] args){
        Scanner input=new Scanner(System.in);
        
        do{
            int num=input.nextInt();
            if(fibonacci(num)){
                System.out.println("O número "+num+" pertence a sequência de Fibonacci");
            }else{
                System.out.println("O número "+num+" não pertence a sequência de Fibonacci");
            }
        }while(input.toString()!="");
        input.close();

    }
}