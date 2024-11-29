

const request = ()=> {
  url = "try"

  try{

    fetch(url)
    .then (
       if(!Response.ok){
        console.log(succesfull)
       } 
    )
    .then( response=>response.json()
    .then(json=>Data.json())


    )
  }
  catch{}



  


}

const request = () => {
    const url = "try"; // Assuming you will replace "try" with a valid URL
  
    fetch(url)
      .then(response => {
        if (!response.ok) {
          throw new Error("Network response was not ok"); // Throw an error for non-200 responses
        }
        return response.json(); // Return the JSON data
      })
      .then(data => {
        console.log(data); // Log the retrieved data
      })
      .catch(error => {
        console.error("Fetch error:", error); // Handle any errors
      });
  };
  
  export default request;