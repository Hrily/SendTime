/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.IOException;
import java.io.PrintWriter;
import java.util.Calendar;
import java.util.GregorianCalendar;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 *
 * @author hrishi
 */
@WebServlet(urlPatterns = {"/SendTime"})
// Extend HttpServlet class
public class SendTime extends HttpServlet {

	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
	
		//content type must be set to text/event-stream
		response.setContentType("text/event-stream");	

		//encoding must be set to UTF-8
		response.setCharacterEncoding("UTF-8");

		PrintWriter writer = response.getWriter();

		for(int i=0; i<=30; i++) {

                        writer.write("event: timestamp\n");
			writer.write("data: "+ System.currentTimeMillis() +"\n\n");
                            
                	try {
                                writer.flush();
                                Thread.sleep(2000);
			} catch (InterruptedException e) {
                		e.printStackTrace();
                        }
                        
		}
                writer.write("event: DONE\ndata: NA\n\n");
                writer.flush();
		//writer.close();
                
	}
}