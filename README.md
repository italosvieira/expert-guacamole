# expert-guacamole

Project uses poetry for dependency management. poetry install to install dependencies.

Run main to create the csv file.

Its super slow beacuse for each movie it actually runs another request synchronously and await for the response, didnt have time to improve performance.

The data.csv only have the first two lines with the real data beacause i couldnt run the script full because i ran out of time.

The are some minor bugs with movies that have complex titles so thats what the try catch is doing. Didn have time to fix those either.