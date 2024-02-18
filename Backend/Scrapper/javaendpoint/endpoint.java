package javaendpoint;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class endpoint{

    private String ip_address = "http://38.56.138.77:8888/service/";
   
    public String get_images_on_address(String address){
        String url = this.ip_address + address;
        HttpClient client = HttpClient.newHttpClient(); 
        HttpRequest request = HttpRequest.newBuilder().GET().header("accept", "application.json").uri(URI.create(url)).build();
        HttpResponse<String> response; 

        try{
            response = client.send(request, HttpResponse.BodyHandlers.ofString());
            System.out.println(response.body());
            return response.body();
            
        } catch(Exception e){
            System.out.println("couldn't make request");
            return "False"; 
        }
        
    }
}