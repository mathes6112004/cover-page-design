# COVER PAGE DESIGN USING HTML AND CSS


## AIM:
To design a website to create a webpage displaying the cover page of the book "Responsive Web Design with HTML5 and CSS".

## DESIGN STEPS:

### Step 1:
Create a new Django project using  "django-admin startproject",get into the project terminal  and use "python3 manage.py startapp" command.
 
### Step 2:
Define  urls.py and views.py for the website .Allow host access and add the app name under installed apps in settings.py


### Step 3:
Create a templates folder under the app folder followed by a folder under templates with the app name followed by html file named bookdesign.html


### Step 4:
Write HTML and CSS code in the file save it and run the app using python manage.py makemigrations and python manage.py migrate commands .Run the Server using "python3 manage.py runserver 0:80" command.

### STEP 5:-
The Website is published.We created a webpage displaying the cover page of the book "Responsive Web Design with HTML5 and CSS".



## PROGRAM :
# BOOKDESIGN.HTML
```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title> Responsive Web Design with HTML5 and CSS</title>
        <style>
        h1{
           color:white;
        }
         .bookpage{
             width: 400px;
             height: 600px;
             
             margin-left: auto;
             margin-right: auto ;
             padding: 20px;
             background-image: url('/static/images/dna1.jpg');
  background-size: cover;
  background-repeat: no-repeat;
         }
         .toptext{
             color:white;
             padding-left: 5px;
             font-size: 14px;
             font-family: Arial, Helvetica, sans-serif;
             
         }
         .tophr{
             color:#e36f2f;
              width: 180px;
         }
         hr{
             color:#e36f2f;
            
         }
         .booktitle{
             font-family: Arial, Helvetica, sans-serif;
             padding: 10px 10px 0px 10px;
             display: flex;
            align-items: center;
            justify-content: center;
  margin-right: 10px;
  margin-left: 10px;
  font-size: 20px;
         }
         .author{
             color:white;
             font-family: Arial, Helvetica, sans-serif;
             display: inline;
              font-size: 24px;
              
             
         }
         .sub-text {
             color:white;
             font-family: Arial, Helvetica, sans-serif;
              display: flex;
            
            
  margin-right: 10px;
  margin-left: 10px;

  font-size: 14px;
  }
  
.footer {
  
  padding-top: 90px;
}
.image {
    color:white;
             font-family: Arial, Helvetica, sans-serif;
 font-size: 22px;
  margin-right: 20px;
}
.bottomhr { 
    color:#e36f2f;
              width: 400px;

}
img {
    width: 90px;
    height: 100px;
    margin-right: 20px;
    vertical-align: bottom;
}
.edition {
    color:#e36f2f;
             font-family: Arial, Helvetica, sans-serif;
 font-size: 22px;
 line-height: 20px;
 
}


        </style>
        </head>
            <body>
                <div class="bookpage">
                    
                    <div class="toptext">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EXPERT DESIGN</div>
                    <div class="tophr"><hr></div> 
               <div class="booktitle"><h1> Responsive Web Design with HTML5 and CSS </h1></div>
               <h3 class="sub-text">Develop future proof responsive websites</h3>
                    <h3 class="sub-text">using latest HTML and CSS designs</h3>
                    <div class="footer">
                        <h2 class="edition">&nbsp;&nbsp;Third Edition&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  <img src="/static/images/ben1.jpg" alt="Author Image"></h2>
                      
                        <div class="bottomhr"><hr></div>
                    <div class="author"><h3>&nbsp;&nbsp;Ben Frain &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Packt></h3></div>
                    
                </div>
                </div> 
                
            </body>
        
    
</html>

     
```


## OUTPUT:
### Home Page:
![Screenshot (85)](https://user-images.githubusercontent.com/118343379/212694283-e1f36876-94c2-4ba8-8eb3-14fba8be2d26.png)



## Result:
Successfully designed a website to display the cover page of the book "Responsive Web Design with HTML5 and CSS".


