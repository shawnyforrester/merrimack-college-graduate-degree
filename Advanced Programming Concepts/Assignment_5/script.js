async function getWeather() {
  let officeId = document.getElementById("office_id").value;
  let gridX = document.getElementById("grid_x").value;
  let gridY = document.getElementById("grid_y").value;
  const url = `https://api.weather.gov/gridpoints/${officeId}/${gridX},${gridY}/forecast`;
  const foreCast = document.getElementById("forecast");

  try {
    await fetch(url, {
      method: "GET",          
    }).then((response) => response.json())
    .then((data) => {
        // Extracting the relevant data from the API response
        console.log(data)
        let forecast = data.properties.periods[0].detailedForecast;
        let temperature = data.properties.periods[0].temperature;   
        let windSpeed = data.properties.periods[0].windSpeed;
        let windDirection = data.properties.periods[0].windDirection;
    
        // Displaying the data in the HTML elements       
        foreCast.innerHTML = `Today's Forecast:\t ${forecast}`;
        document.getElementById("temperature").innerHTML = `Current Temperature: ${temperature}`;
        document.getElementById("speed").innerHTML = `Current wind speed: ${windSpeed}`;
        document.getElementById("direction").innerHTML = `Current wind direction: ${windDirection}`;
        });  
  } catch (error) {
    console.error(error);
  }
}

async function getLocation(){
    const locationDisplay = document.getElementById("location");
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            function (position) { success(position); },
            function (e) { unsuccess() },
            { enableHighAccuracy: true });
    } else { 
        var t = document.getElementById("coord");
        t.innerHTML = "&nbsp Geolocation is not supported by this browser.";
    }
}
function success(position) {
    var lat = position.coords.latitude;
    var lng = position.coords.longitude;
    var t = document.getElementById("coord");
    t.innerHTML = "&nbsp Latitude: " + Math.round(lat * 100)/100 +
                  " - Longitude: " + Math.round(lng * 100)/100;
    var x = document.getElementById("barv");
    longitude = Math.round(lng+180)*512/180
    x.style.left = longitude+"px"
    x.style.opacity = 0.8
    var y = document.getElementById("barh");
    latitude = Math.round(90-lat)*256/90
    y.style.top = latitude+"px"
    y.style.opacity = 0.8
}
function unsuccess() {
    var t = document.getElementById("coord");
    t.innerHTML = "&nbsp Geolocation was not allowed by the user. "+
                  "This may be a one-time refusal or you need to "+
                  "check the Location Services on your Settings.";
}

