package javaendpoint;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;



public class endpoint{

    private String ip_address = "http://38.56.138.77:8888/service/";
    private String lang_id = "/java";
   
    public String get_images_on_address(String address){

        //FILTER THE ADDRESS AND ADD THE '-' FOR EACH SPACE IN THE ADDRESS
        char[] array = address.toCharArray();

        for(int i = 0; i < address.length(); i++){
            if(array[i] == ' '){
                array[i] = '-';
            }
        }
        address = new String(array);

        String url = this.ip_address + address + this.lang_id;
        System.out.print("URL SENT: ");
        System.out.print(url);
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