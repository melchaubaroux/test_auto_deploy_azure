from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

import uvicorn
import os


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# load images
images_folder = "./images"
metrics_folder = "./metriques"

# Liste des fichiers avec l'extension .png dans le dossier d'images
adresse_image = [
    images_folder + "/" + file
    for file in os.listdir(images_folder)
    if file.endswith(".png")
]

# adresse_image = [file for file in os.listdir("./images/") if file.split(".")[-1]=="png"]
print(f"taille du fichier d'adresse image : {len(adresse_image)}")

# load metrics
# adresse_metrics = [ file for file in os.listdir("./metriques/") if file.split(".")[-1]=="txt"]
adresse_metrics = [
    metrics_folder + "/" + file
    for file in os.listdir(metrics_folder)
    if file.endswith(".txt")
]
print(f"taille du fichier d'adresse metrics : {len(adresse_metrics)}")


# get image
@app.get("/model/{model}")
async def collect_data(model):
    image = [x for x in adresse_image if model in x][-1]
    return FileResponse(image, media_type="image/png")


# get metrics
@app.get("/metric/{model}")
async def collect_data(model):
    metric = [x for x in adresse_metrics if model in x][-1]
    # return "mse"
    return FileResponse(metric, media_type="text/html")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
