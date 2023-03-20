

navigator.geolocation.watchPosition((a)=>{
    x=a.coords.latitude//isse latitude ayega
    y=a.coords.longitude//isse longitude milega
   
    const url1 = `/location`
                $.ajax({
                    data: {
                        latitude:x,
                        longitude:y
                        
                    },
                    url: url1,
                    type: 'POST',
                    success: function (response) {
                        console.log("success")
                    },
                    error: function (response) {
                        console.log("error")

                    }
                });
})
