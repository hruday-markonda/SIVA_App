//--------------------------------------------------------------------------------------------------
//The standard animation used when adding elements is made using JQuery because JQuery has simple animations which are
//more than enough for my application.

micback = document.getElementById("microphonebackground")

function ChangeButton(){
    document.getElementById("OnclickSound").play();
    document.getElementById("microphone").style.filter = "contrast(200%)";
    micback.style.backgroundImage = "linear-gradient(white,white), repeating-conic-gradient(cyan, blue, magenta, red, yellow, lime, cyan)";
    micback.style.animation = "RGB 1s linear infinite normal";

    //the reason why the microphone background display is set to none and then block immediately is because in Safari
    //it is unable to visually update the changes to css animations for some reason
    micback.style.display ="none";
    setTimeout(function(){micback.style.display ="block";},0);
}

//--------------------------------------------------------------------------------------------------
//This is the url change function for my built in video/music player which also acts as an interface to look at google
//results. It updates the link by changing the src value of the iframe with the url given.

function URLchange(url){
    if (url !== "non") {
        document.getElementById("Iframe").src = url;
        $("#Iframe").animate({height: "366px"},{ duration: 3000, queue: false });
        $("#Webframe").animate({height: "370px"},{ duration: 3000, queue: false });
        $("#textbox").animate({height: "180px"},{ duration: 3000, queue: false });
    }
}

//--------------------------------------------------------------------------------------------------
//This is the weather function. This function processes the Temp and Pic keys and decides based on the values what
//picture to put in the weather box and accompany it with the description of the weather and the temperature to
//accompany it.

function Weather(pic, temp){
    weatherbox = document.getElementById("WeatherBox");
    weatherpic = document.getElementById("WeatherPic");
    weathertemp = document.getElementById("WeatherTemp");
    weatherdesc = document.getElementById("WeatherDesc");
    if (temp !== "non" && pic !== "non"){
        if (pic.includes("Cloudy") || pic.includes("cloudy")){
            weatherpic.src = "static/photos/cloudy.png";
        }
        else if (pic.includes("Sunny") || pic.includes("Clear") || pic.includes("clear")|| pic.includes("sunny")){
            weatherpic.src = "static/photos/sunny.png";
        }
        else if (pic.includes("Rain") || pic.includes("Thunderstorm") || pic.includes("Showers") || pic.includes("rain") || pic.includes("thunderstorm") || pic.includes("showers")){
            weatherpic.src = "static/photos/rainy.png";
        }
        weathertemp.innerText = "The temperature is: "+ temp;
        weatherdesc.innerText = "Weather Condition: " + pic;
        $("#textbox").animate({height: "485px", marginTop: "74px"}, { duration: 3000, queue: false });
        setTimeout(function(){$("#WeatherBox").show(3000)}, 2000);
    }
    else{}
}

//--------------------------------------------------------------------------------------------------
//This function is what my recieved JSON from my python server will be passed into to visually show the results. This
//function every single gets the JSON input will add a HTML element inside the textbox div tag where if the USERTEXT key
//is empty then it only add's SIVA's response else it adds both the user input and SIVA's response with a delay between
//the messages being added.

function ChangeHTML(MyJson){
    var RecievedJson = JSON.parse(MyJson)
    DialogBox = document.getElementById("textbox");
    if (RecievedJson.USERTEXT === "non") {
         DialogBox.insertAdjacentHTML('beforeend', '<div><div><h2 class="SivaMessage"><a style="color:cyan;">SIVA: </a>' + RecievedJson.SIVATEXT + '</h2></div></div><hr>');
    }
    else{
        DialogBox.insertAdjacentHTML('beforeend', '<div><div><h2 class="UserMessage"><a style="color:orangered;">User: </a>' + RecievedJson.USERTEXT + '</h2></div></div><hr>');
        setTimeout(function(){DialogBox.insertAdjacentHTML('beforeend','<div><div><h2 id="text1" class="SivaMessage"><a style="color:cyan;">SIVA: </a>' + RecievedJson.SIVATEXT + '</h2></div></div><hr>')}, 1000);
    }
    Weather(RecievedJson.WEATHERIMAGE, RecievedJson.TEMP);
    URLchange(RecievedJson.WEBLINK);
    document.getElementById("microphone").style.filter = "contrast(200%) invert(100%)";
    micback.style.backgroundImage = "linear-gradient(black,black), repeating-conic-gradient(cyan, blue, magenta, red, yellow, lime, cyan)";
    micback.style.animation = "RGB 3s linear infinite normal";

    //the reason why the microphone background display is set to none and then block immediately is because in Safari
    //it is unable to visually update the changes to css animations without refreshing the display of the object for
    //some reason

    micback.style.display ="none";
    setTimeout(function(){micback.style.display ="block";},0);

    if (RecievedJson.APPSTAT !== "non"){
        setTimeout(function(){$("body *").fadeOut("slow")},2200);
        setTimeout(function(){$.get('/closeApp/',function(){});},3600);
    }
}

//--------------------------------------------------------------------------------------------------
//This function runs every single time the input button is pressed to restore the original interface.

function resetHTML(){
    $("#WeatherBox").hide(1500).dequeue;
    $("#Iframe").animate({height: 0}, { duration: 3000, queue: false });
    $("#Webframe").animate({height: 0}, { duration: 3000, queue: false });
    setTimeout(function(){$("#textbox").animate( {height: "541px", marginTop: "14px"}, { duration: 3000, queue: false })}, 1000);
    setTimeout(function(){document.getElementById("Iframe").src = ""},1500);
}

//--------------------------------------------------------------------------------------------------
//--------------------------------------------------------------------------------------------------