from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.properties import NumericProperty
from chemicalGUIManager import chemicalInputInterpreter
from chemicalGUIManager import chemicalFileReader
from chemicalGUIManager import chemicalDictHandler
from chemicalReaction import chemicalCalculator
from userInputDict import userInputDict

from kivy.config import Config
Config.set('graphics', 'multisamples', '0')

'''
    ONLY SINGLE SCREEN.

    class hierarchy:
    root: boxlayout
        - gridlayout
            - BoxLayout
                - label * 3
            - gridlayout
                - image * 3
        - boxlayout
            - textinput
'''

molDict = userInputDict({})
velDict = userInputDict({})

class RootLayout(BoxLayout):
    
    element = ListProperty()

class ChemStatusViewer(BoxLayout):
    
    reactionSpeed = StringProperty("0")
    ReactionDegree = StringProperty("0")
    ReactionVelocityConst = StringProperty("0")

    def setReactionSpeed(self, newValue):
        self.reactionSpeed = newValue

    def setReactionDegree(self, newValue):
        self.ReactionDegree = newValue

    def setReactionVelocityConst(self, newValue):
        self.ReactionVelocityConst = newValue

    def getReactionSpeed(self):
        return self.reactionSpeed

    def getReactionDegree(self):
        return self.ReactionDegree

    def getReactionVelocityConst(self):
        return self.ReactionVelocityConst

class ChemReactionFormulaInput(BoxLayout):

    def elementalize(self):

        elements = chemicalInputInterpreter.toElement(self.ids.chemText.text)
        elements = chemicalInputInterpreter.removeQuotient(elements)
        self.parent.element = elements

        # Violates One-function-for-one-method rule.
        self.parent.ids.molGrid.createMolarityTable()
        self.parent.ids.velGrid.createVelocityTable()

    '''
    def elementalizeInput(self):

        print(root.ids.molGrid)
        elements = chemicalInputInterpreter.toElement(self.ids.chemText.text)
        elements = chemicalInputInterpreter.removeQuotient(elements)
        self.parent.element = elements
        print("Elementalized successfully.")

    def molarityInput(self):

        temp = ChemMolarityInputGrid()
        temp.createMolarityTable()
    '''

    '''
    except (TypeError, AssertionError) as e:
        print(e)
        self.ids.chemText.text = ""
        self.ids.chemText.hint_text = "Not a valid chemical equation! Please try with valid one."
    '''

class ChemMolarityInputGrid(GridLayout):

    def createMolarityTable(self):

        for row in range(0, 4):
            for col in range(0, 3):
                if row == 0 and col == 0:
                    self.add_widget(Button(size_hint=(.1,.1)))
                if row == 0 and col != 0:
                    self.add_widget(Button(text=str(self.parent.parent.element[col-1]), size_hint=(.1, .1)))
                if row != 0 and col == 0:
                    self.add_widget(Button(text=str(row), size_hint=(.1,.1)))
                if row !=0 and col != 0:
                    mi = ChemMolarityInput(size_hint=(.1,.1), multiline=False)
                    mi.set_order([col-1, row-1])
                    self.add_widget(mi)
                    # self.add_widget(molInput)

class ChemVelocityInputGrid(GridLayout):

    def createVelocityTable(self):

        for row in range(0, 4):
            for col in range(0, 2):
                if row == 0 and col == 0:
                    self.add_widget(Button(size_hint=(.1,.1)))
                if row == 0 and col != 0:
                    self.add_widget(Button(text="Velocity", size_hint=(.1, .1)))
                if row != 0 and col == 0:
                    self.add_widget(Button(text=str(row), size_hint=(.1,.1)))
                if row !=0 and col != 0:
                    vi = ChemVelocityInput(size_hint=(.1,.1), multiline=False)
                    vi.set_order([col-1, row-1])
                    self.add_widget(vi)

        # print("Parent is " + str(self.parent))

        # Must be distinguished with 'cols' and 'rows'
        '''
        self.cols = (len(self.parent.element) + 1)
        self.rows = (len(self.parent.element) + 2)
        print(self.cols)
        print(self.rows)
        print("Whoami : " + str(self))
        '''

        '''
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                print("Iterating through...")
                if row == 0 and col == 0:
                    self.add_widget(Button(size_hint=(.1,.1)))
                if row == 0 and col != 0:
                    self.add_widget(Button(text=str(self.parent.element[col-1]), size_hint=(.1, .1)))
                if row != 0 and col == 0:
                    self.add_widget(Button(text=str(row), size_hint=(.1,.1)))
                if row !=0 and col != 0:
                    molInput = ChemMolarityInput()
                    molInput.bind(text = on_text)
                    self.add_widget(molInput)
        '''

class ChemMolarityInput(TextInput):

    order = ListProperty([])

    def __init__(self, **kwargs):
        super(ChemMolarityInput, self).__init__(kwargs)
        for i in range(0, 3):
            molDict.appendDictElement([0,0], i)

    # def on_text(instance, value):
    #    print("Value has been changed into " + str(value))

    def set_order(self, value):
        self.order = value

    def get_order(self):
        return self.order

    def on_text(self, instance, text):
        print("Text from " + str(instance) + " : " + str(text))

class ChemVelocityInput(TextInput):
    
    order = ListProperty([])

    def __init__(self, **kwargs):
        super(ChemVelocityInput, self).__init__(kwargs)
        for i in range(0, 3):
            velDict.appendDictElement(0, i)

    def set_order(self, value):
        self.order = value

    def get_order(self):
        return self.order

    def on_text(self, instance, text):
        print("Text from " + str(instance) + " : " + str(text))


root = Builder.load_string('''
RootLayout:
    orientation: 'vertical'

    BoxLayout:
        id: subLayout
        orientation: 'horizontal'

        ChemMolarityInputGrid:
            id: molGrid
        ChemVelocityInputGrid:
            id: velGrid
        ChemStatusViewer:

    ChemReactionFormulaInput:

<ChemMolarityInputGrid>:
    cols: 3
    rows: 4
    width: root.parent.width/4
    height: root.parent.height/4
    size_hint_x: .3
    size_hint_y: .3

<ChemVelocityInputGrid>:
    cols: 2
    rows: 4
    width: root.parent.width/4
    height: root.parent.height/4
    size_hint_x: .2
    size_hint_y: .3

<ChemStatusViewer>:
    orientation: 'vertical'
    size_hint_y: None
    width: root.parent.width/2

    Label:
        halign: 'right'
        text_size: self.size
        text: "Reaction Speed(v) : " + root.getReactionSpeed()
    Label:
        halign: 'right'
        text_size: self.size
        text: "Reaction degree(x, y) : " + root.getReactionDegree()
    Label:
        halign: 'right'
        text_size: self.size
        text: "Reaction velocity constant : " + root.getReactionVelocityConst()

<ChemReactionFormulaInput>:
    orientation: 'vertical'
    width: self.parent.width
    size_hint_y: None

    TextInput:
        id: chemText
        hint_text: "Please input chemical reaction formula, like 2H2 + O2 -> 2H2O"
        font_size: 20
        multiline: False
        on_text_validate: self.parent.elementalize()
''')

class chemReactionSpeedCalculator(App):

    def build(self):
        chemicalFileReader.read_chem_files()
        return root

if __name__ == "__main__":
    chemReactionSpeedCalculator().run()
    
    
