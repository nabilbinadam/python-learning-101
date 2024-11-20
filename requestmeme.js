
/* async= perkara yang lambat datang. sebab web ni kalau buat request tak semestinya datang terus. */ 



url="https://api.imgflip.com/get_memes"
  
try{
    const response = fetch(url)
    .then(console.log(response))
    .then(json(response))
    .then(return )

    if response == "Success"{

        console.log("success")
    }

    return response.json()
    

}

catch
{
console.error("Error 404",error);

}


