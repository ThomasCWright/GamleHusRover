from kivy.utils import platform
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

import kivy

kivy.require('2.0.0')

# if platform == 'android':
    # from android.permissions import Permission, request_permissions
    # from android.storage import primary_external_storage_path

class CardinalMotionScreen(BoxLayout):
    '''screen to control csrdinal motion of rover'''
    def __init__(self):
        super(CardinalMotionScreen, self).__init__()
    
    def build(self):
        pass

class RoverMotion(App):
    ''' main app for controlling rover motion'''

    def build(self):
        # if platform == 'android':
        #     request_permissions([Permission.WRITE_EXTERNAL_STORAGE,
        #                 Permission.READ_EXTERNAL_STORAGE])
        return CardinalMotionScreen()

def init():
    if __name__ == '__main__':
        RoverMotion().run()
        return 42 

init()