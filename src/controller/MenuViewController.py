import pygame
from requests import get
from model.Player import Player
from services.SocketClient import SocketClient
from services.SocketServer import SocketServer
from view.MenuView import MenuView


class MenuViewController:
    def __init__(self):
        pygame.init()
        self.player = Player()
        self.menu_view = MenuView(self)
        self.socket_client = SocketClient()
        self.socket_server = SocketServer()
        self.ip_public = 'nur mit Windows'
        # Funktioniert aktuell noch nicht mit MacOS!
        #self.ip_public = get('https://api.ipfy.org').content.decode('utf8')
        self.temp_server_ip = 'HALLOOOOOOOOOOOO MAX I BIMS'

    def start_game(self):
        pass

    def set_player_name(self, value):
        self.player.username = value

    def set_is_player_host(self, value, is_player_host):
        self.player.is_host = is_player_host
        print(is_player_host)
        print(value)

    def show_menu(self):
        self.menu_view.draw_username_input()

    def show_connect_menu(self):
        print(self.player.username)
        print(self.player.is_host)
        if self.player.is_host:
            self.socket_server.run_server()
            self.socket_client.server_ip = self.socket_server.ip
            if self.socket_client.connect() == 'connected':
                print('Alles tutti')
            else:
                print('Verkackt!!! du ARSCHLOCH 1')

        self.menu_view.draw_connect_player(self.player.is_host, self.socket_server.ip, self.ip_public)

    def set_temp_server_ip(self, value):
        print(self.temp_server_ip)
        self.temp_server_ip = value
        print(self.temp_server_ip)

    def connect_to_host(self):
        self.socket_client.server_ip = self.temp_server_ip
        if self.socket_client.connect() == 'connected':
            print('Verbindung zustande gekommen')
        else:
            print('Verkackt!!! du ARSCHLOCH 2')


if __name__ == '__main__':
    mvcon = MenuViewController()
    mvcon.show_menu()
