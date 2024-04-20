from tkinter import* # We import the Tkinter library
from PIL import ImageTk, Image # We import ImageTk and Image modules from the PIL library
import requests# We import the requests library
url='https://api.openweathermap.org/data/2.5/weather'# define the URL of the weather API
api_key='-----------------------------------'#We define the API key this key  OpenWeatherMap you can register on the website and get
icon_url='https://openweathermap.org/img/wn/{}@2x.png'# We define the URL of the weather icon

def getWeather(city):# We define the getWeather function
    params = {'q':city,'appid':api_key,'lang':'tr'}# We define the parameters of the API request
    data=requests.get(url,params=params).json()# We send a request to the API and get the data in JSON format
    if data:# If there is data in the response
        city=data['name'].capitalize()# We get the city name and capitalize it
        country= data['sys']['country']# We get the country name
        temp= int(data['main']['temp']-273.15)# We get the temperature and convert it to Celsius
        icon= data['weather'][0]['icon']# We get the weather icon
        condition= data['weather'][0]['description']# We get the weather condition
        return (city,country,temp,icon,condition)# We return the city name, country name, temperature, weather icon, and weather condition

def main(event=None):# We define the main function and with the parameter event=None we will make it work when the Enter key is pressed from the keyboard
        city=cityEntry.get()# We get the city name from the entry box
        weather_data=getWeather(city)# We get the weather data by calling the getWeather function with the entered city name
        if weather_data:# If there is weather data
            locationLabel ['text']='{},{}'.format(weather_data[0],weather_data[1])# We print city name and country name
            tempLabel ['text']='{} °C'.format(weather_data[2])# We print the temperature data, we add the °C sign, we can do it by pressing the alt + 0176 keys
            conditionLabel ['text']=weather_data[4]# We print the weather condition
            icon=ImageTk.PhotoImage(Image.open(requests.get(icon_url.format(weather_data[3]),stream=True).raw))# We get the weather icon on the label
            iconLabel.configure(image=icon)# We show the weather icon
            locationLabel.image=icon# We show the weather icon on the label


app=Tk()# We create the application window
app.geometry('300x450')# We set the size of the application window
app.title(' Weather  ')# We set the title of the application window

cityEntry=Entry(app,justify='center')#  We create an entry box for the city name
cityEntry.pack( fill=BOTH, ipady=10,padx=18, pady=5)# We place the entry box on the screen
cityEntry.focus()#  We set the focus to the entry box

searchButton=Button(app,text='Arama',font=('Arial',15),command=main)# We create a search button
searchButton.pack(fill=BOTH, ipady=10, padx=20)#  We place the search button on the screen

iconLabel=Label(app)# We create a label to show the weather icon
iconLabel.pack()#  We place the weather icon on the screen

locationLabel=Label(app,font=('Arial',40))#  We create a label to show the city name and country name
locationLabel.pack()#  We place the city name and country name on the screen

tempLabel=Label(app,font=('Arial',50,'bold'))#   We create a label to show the temperature data
tempLabel.pack()#  We place the temperature data on the screen
conditionLabel=Label(app,font=('Arial',20))#  We create a label to show the weather condition
conditionLabel.pack()# We place the weather condition on the screen

app.bind('<Return>', main)# We bind the Enter key to the main function
app.mainloop()# We run the application window