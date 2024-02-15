

public class RedfinBot{

    String name = "";
    boolean status = false;

    RedfinBot(){
        this.name = "";
        this.status = false; 
    }

    public static void main(String[] args){
        System.out.println("hello world");
    }

    void run(){
        System.out.println("You ran the bot");
    }

    void stop(){
        System.out.println("You stopped the bot");
    }

    void set_name(String name){
        this.name = name;    
    }

    void set_true(){
        this.status = true; 
    }

    void set_false(){
        this.status = false; 
    }

}