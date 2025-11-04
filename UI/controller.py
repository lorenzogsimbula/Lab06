import flet as ft
from UI.view import View
from model.model import Autonoleggio
from UI.alert import AlertManager

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view : View, model : Autonoleggio):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    # TODO

    def mostra(self,e):
        """
        try:
            auto=self._model.get_automobili() or []
            self._view.lista_auto.controls.clear()
            if not auto:
                self._view.lista_auto.controls.append(ft.Text("Nessun automobile trovata."))
            else:
                for a in auto:
                    self._view.lista_auto.controls.append(self._render_auto_tile(a))
            self._view.update()
        except Exception as ex:
             self._view.show_alert(f"Error: {ex}")
             """
        lista = self._model.get_automobili()

        for auto in lista:
            self._view.lista_auto.controls.append(ft.Text(auto))
        self._view.update()


    def cerca(self,e):
        modello = (self._view.input_modello_auto.value or "").capitalize()

        """
        try:
            results = self._model.cerca_automobili_per_modello(modello) or []
            self._view.lista_auto.controls.clear()
            if not results:
                self._view.lista_auto_ricerca.controls.append(ft.Text("Nessun risultato."))
            else:
                for a in results:
                    self._view.lista_auto_ricerca.controls.append(self._render_auto_tile(a))

            self._view.update()

        except Exception as ex:
            self._view.show_alert(f"Errore durante la ricerca: {ex}")"""

        lista = self._model.get_automobili() or []
        for auto in lista:
            if auto.modello == modello:
                self._view.lista_auto_ricerca.controls.append(ft.Text(auto))
            self._view.update()
        if len(self._view.lista_auto_ricerca.controls) == 0:
            raise Exception(self._alert.show_alert("Modello non presente"))




