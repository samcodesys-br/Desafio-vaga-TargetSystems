import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner input=new Scanner(System.in);
        
        do{
            char[] string=input.nextLine().toCharArray();
            char[] reverse=new char[string.length];
            for(int i=string.length-1,j=0;i>=0;i--,j++){
                reverse[j]=string[i];
            }
            System.out.println(reverse);
        }while(!input.equals(""));
        input.close();

    }
}