package javaendpoint;
import javaendpoint.endpoint; 

public class sample {
    public static void main(String[] args){
        endpoint api = new endpoint(); 
        String response = api.get_images_on_address("6330 Elmhurst Dr, San Diego, CA");

        //Need to add slashes or something so the webserver can parse the request
        System.out.println(response);
    }
}
