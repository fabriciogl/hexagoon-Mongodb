# Copyright (c) 2021. QuickTest. App de estudo por questões. Criador: Fabricio Gatto Lourençone. Todos os
# direitos reservados.

import uvicorn
from fastapi import FastAPI

from Entrypoints import QuestaoEntrypoints, UsuarioEntrypoints, TesteEntrypoints
from Excecoes.ExceptionHandlers import invalid_id, not_found
from Excecoes.GenericValidationExceptions import InvalidIdException
from Excecoes.MongoExceptions import MongoFindException2
from Repositorio.Mongo.Configuracao.MongoSetupAssincrono import MongoSetupAssincrono
from Repositorio.Mongo.Configuracao.MongoSetupSincrono import MongoSetupSincrono

app = FastAPI()

app.include_router(QuestaoEntrypoints.router)
app.include_router(UsuarioEntrypoints.router)
app.include_router(TesteEntrypoints.router)

app.add_event_handler("startup", MongoSetupAssincrono.connect_db)
app.add_event_handler("startup", MongoSetupSincrono.connect_db)
app.add_event_handler("shutdown", MongoSetupAssincrono.close_db)


app.add_exception_handler(InvalidIdException, invalid_id)
app.add_exception_handler(MongoFindException2, not_found)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
