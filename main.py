



from kivy import config
import kivy
from kivy.config import Config
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.uix.pagelayout import PageLayout
from kivy.properties import StringProperty, BooleanProperty,NumericProperty,Clock
from kivy.graphics import Rectangle, Color
from kivy.graphics.vertex_instructions import Line,Ellipse,Quad
from kivy.properties import Clock
from kivy.graphics.context_instructions import Color
from kivy.config import Config
from kivy.core.audio import Sound, SoundLoader
from kivy.lang import Builder
import random
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy import platform
from kivy.properties import NumericProperty, Clock, ObjectProperty, StringProperty





































class MainExample(GridLayout):
    menu_widget = ObjectProperty()
    my_text = StringProperty("hello1!")
    text_input_str=StringProperty("hello1!")
    text_input_str1=StringProperty("0")
    text_input_str2=StringProperty("0")
    text_input_str3=StringProperty("0")
   
    count_enabled = BooleanProperty(False)
    pos_number=2
    
   
    
    comparenumber=[]
    comparenumberint=0
    minvalue=StringProperty("0")
    maxvalue=StringProperty("100")
    minvaluecom=0
    maxvaluecom=100
  

    no0=None
    no1=None
    no2=None
    no3=None
    no4=None
    no5=None
    no6=None
    no7=None
    no8=None
    no9=None
    
    newrandomnumb=0
  
    

    def __init__(self, **kwargs):
        super(MainExample,self).__init__(**kwargs)

        self.init_sound()
   
   
        
    def rand(self):
    
        
        comparenumber=random.randint(0,100)
        x = [int(a) for a in str(comparenumber)]        
        
        if comparenumber==100:
            self.text_input_str1=str(x[0])
            self.text_input_str2=str(x[1])
            self.text_input_str3=str(x[2])
        if 9<comparenumber<100:
            self.text_input_str2=str(x[0])
            self.text_input_str3=str(x[1])
            self.text_input_str1='0'
        if comparenumber<=9:
            self.text_input_str3=str(x[0])
            self.text_input_str1='0'
            self.text_input_str2='0'
            

    def back(self):
        
        self.pos_number=2
        self.comparenumber=[self.text_input_str1,   self.text_input_str2,      self.text_input_str3]
        
        self.text_input_str3=self.text_input_str2
        self.text_input_str2=self.text_input_str1
        self.text_input_str1='0'
        self.comparenumber=[self.text_input_str1,   self.text_input_str2,      self.text_input_str3]
        
        
            
    
        
          
    def init_sound(self):
         
        self.sound_boom = SoundLoader.load("audio/boom.wav")    
        self.no0=SoundLoader.load("audio/0.wav")
        self.no1=SoundLoader.load("audio/1.wav")
        self.no2=SoundLoader.load("audio/2.wav")
        self.no3=SoundLoader.load("audio/3.wav")
        self.no4=SoundLoader.load("audio/4.wav")
        self.no5=SoundLoader.load("audio/5.wav")
        self.no6=SoundLoader.load("audio/6.wav")
        self.no7=SoundLoader.load("audio/7.wav")
        self.no8=SoundLoader.load("audio/8.wav")
        self.no9=SoundLoader.load("audio/9.wav")
        
       
        self.sound_boom.volume=1
        
    
            
        
    def enter(self):
        self.comparenumber=[self.text_input_str1,   self.text_input_str2,      self.text_input_str3]
        strings = [str(self.comparenumber) for self.comparenumber in self.comparenumber]
        a_string = "".join(strings)
        an_integer = int(a_string)     

        print(self.parent.newrandomnumb)
        print(an_integer)
   
        if  an_integer>self.minvaluecom:
            if an_integer<self.parent.newrandomnumb and an_integer>=0:
                    self.minvalue=str(an_integer)
                    self.minvaluecom=an_integer
        if  an_integer<self.maxvaluecom :      
            if  an_integer>self.parent.newrandomnumb and an_integer<=100:
                    self.maxvalue=str(an_integer)
                    self.maxvaluecom=an_integer
        if an_integer==self.parent.newrandomnumb:
                
                print("gameover")
                self.parent.changeimage="images/cake2.jpg"
                self.sound_boom.play()
               
                
                self.parent.opacitystate=1
                self.parent.disabledstate=False
                self.menu_title="G A M E O V E R"
                self.maxvalue='100'
                self.minvalue='0'
                self.parent.menu_button_title ="R E S T A R T"
                
                self.maxvaluecom=100
                self.minvaluecom=0
                self.parent.newrandomnumb=random.randint(0,100)
                self.parent.buttondisabledstate=True    
                self.parent.gameoverstate= 0
                print(self.parent.gameoverstate)
        self.pos_number=2
        self.text_input_str1='0'
        self.text_input_str2='0'
        self.text_input_str3='0'
        

    def number1(self):
        self.no1.play()
        self.pos_number+=1
        print(self.pos_number)

        self.text_input_str1=self.text_input_str2
        self.text_input_str2=self.text_input_str3
        self.text_input_str3="1"

    def number2(self):
        self.no2.play()
        self.pos_number+=1
        print(self.pos_number)
     
        self.text_input_str1=self.text_input_str2
        self.text_input_str2=self.text_input_str3
        self.text_input_str3="2"
    def number3(self):
        self.no3.play()
        self.pos_number+=1
        print(self.pos_number)
   
            
        self.text_input_str1=self.text_input_str2
        self.text_input_str2=self.text_input_str3
        self.text_input_str3="3"
    def number4(self):
        self.no4.play()
        self.pos_number+=1
        print(self.pos_number)
   
        self.text_input_str1=self.text_input_str2
        self.text_input_str2=self.text_input_str3
        self.text_input_str3="4"
    def number5(self):
        self.no5.play()
        self.pos_number+=1
        print(self.pos_number)
   
        self.text_input_str1=self.text_input_str2
        self.text_input_str2=self.text_input_str3
        self.text_input_str3="5"
    def number6(self):
        self.no6.play()
        self.pos_number+=1
        print(self.pos_number)
  
        self.text_input_str1=self.text_input_str2
        self.text_input_str2=self.text_input_str3
        self.text_input_str3="6"
    def number7(self):
        self.no7.play()
        self.pos_number+=1
        print(self.pos_number)
    
        self.text_input_str1=self.text_input_str2
        self.text_input_str2=self.text_input_str3
        self.text_input_str3="7"
    def number8(self):
        self.no8.play()
        self.pos_number+=1
        print(self.pos_number)
  
        self.text_input_str1=self.text_input_str2
        self.text_input_str2=self.text_input_str3
        self.text_input_str3="8"
    def number9(self):
        self.no9.play()
        self.pos_number+=1
        print(self.pos_number)
    
        self.text_input_str1=self.text_input_str2
        self.text_input_str2=self.text_input_str3
        self.text_input_str3="9"
    def number0(self):
        self.no0.play()
        self.pos_number+=1
        print(self.pos_number)
   
        self.text_input_str1=self.text_input_str2
        self.text_input_str2=self.text_input_str3
        self.text_input_str3="0"

   



















class BoxLayoutMenu(BoxLayout):


  
    def on_menu_button_pressed(self):
        self.parent.opacitystate=0
        self.parent.disabledstate=True
        self.parent.newrandomnumb=random.randint(0,100)
        print(self.parent.opacitystate)
        print(self.parent.newrandomnumb)
        self.parent.music2.play()
  
        self.parent.buttondisabledstate=False
        if self.parent.gameoverstate== 1:
            self.parent.sound_begin.play()
        else:
            self.parent.sound_restart.play()

    
    
class GridLayoutExampletop(BoxLayout):
    pass
class GridLayoutExamplebtm(GridLayout):
    pass
    
class GridLayoutExamplemid(BoxLayout):
    pass
class MainExample2(AnchorLayout):
    menu_widget = ObjectProperty()
    menu_title = StringProperty("BOOM")
    menu_button_title = StringProperty("START")
  
    changeimage=StringProperty("images/boom.jfif")
    opacitystate=ObjectProperty('1')
    buttondisabledstate=BooleanProperty(False)
    disabledstate=BooleanProperty(False)
    newrandomnumb=random.randint(0,100)
    music1=None
    music2=None
    sound_begin=None
    sound_restart=None
    gameoverstate=1
    def __init__(self, **kwargs):
        super(MainExample2,self).__init__(**kwargs)

        self.init_sound()
  
    def init_sound(self):
        self.music1=SoundLoader.load("audio/music1.wav")
        self.music2=SoundLoader.load("audio/music2.wav")
        self.sound_begin = SoundLoader.load("audio/begin.wav")    
        self.sound_restart = SoundLoader.load("audio/restart.wav")   

class boom(App):
    # pass
    def build(self):
        return MainExample2()
    


boom().run()