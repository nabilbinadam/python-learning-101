



const memeCalling= ()=> {

    url="http://127.0.0.1:5000/memelist"

    try{
      fetch(url)
      .then(response=>response.json()
      .then(
        if (!response.ok) 
            console.log("Error!")
      )
      .then(json=>console.log(json))
      .then(json=>json.data.meme)

      )



    }
    catch{}




}

export default CallingMeme  ;
/* 


{"data":{"memes":[{"box_count":2,"captions":1336000,"height":1200,"id":"181913649","name":"Drake Hotline Bling","url":"https://i.imgflip.com/30b1gx.jpg","width":1200},
{"box_count":3,"captions":1048000,"height":908,"id":"87743020","name":"Two Buttons","url":"https://i.imgflip.com/1g8my4.jpg","width":600},


*/