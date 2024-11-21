

const request = () => {

    try {
        url = "Something"
        fetch(url)
            .then(response => {

                if (!response.ok)
                    throw new error("console.log");
                ;


                return response.json()
            }
            )
            .then(json => data.memes)
        return data
    }


    catch {

    }


}