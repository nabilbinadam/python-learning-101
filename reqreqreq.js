
  const getMeme=()=>{
   
    url="test"
    fetch(url)
    .then(response=>response.json())
    .then(
        if (!response==ok){
            console.error("json not found")
    )
    .then(json=>console.log(json)
    .then(json=>json.data.meme)

  }