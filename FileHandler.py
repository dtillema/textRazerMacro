import Keybord_to_numbers


class FileHandler:

    def __init__(self,
                 file_loc="C:\\Users\\Dan\\Desktop\\input.txt",
                 new_file_loc="C:\\Users\\Dan\\Desktop\\Macro 2.xml"):
        self.file = open(file_loc, "r")
        self.new_file = open(new_file_loc, "w")
        Keybord_to_numbers.keys_to_razer_numbers
        self.delay = 10

    def input_file(self):
        line_of_text = self.file.readline()

        # True While it is not at the end of the text document
        while line_of_text != "":
            # Iterate each charter
            for element in line_of_text:
                # convert charter to the razer numbers
                if element.isupper():
                    self.is_upper(element)
                    print(element) # remove code
                else:
                    self.not_upper(element)
                    print(element) # remove code
            line_of_text = self.file.readline()

    # Puts this at the start of the macro file
    def file_header(self):
        self.new_file.write("""
<?xml version="1.0" encoding="utf-8"?>
<Macro xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <Name>Macro 1</Name>
  <Guid>a7bbbe84-49fc-482d-8895-43191603c068</Guid>
  <MacroEvents>
""".strip())

    # Puts this at the end of the file
    def file_footer(self):
        self.new_file.write("""
  </MacroEvents>
  <IsFolder>false</IsFolder>
  <FolderGuid>00000000-0000-0000-0000-000000000000</FolderGuid>
</Macro>    
""")

    # if the character is upper case it should go here to use the sift key
    def is_upper(self, line):
        print(True)
        self.new_file.write(f"""
             <MacroEvent>
      <Type>1</Type>
        <Delay>{self.delay}</Delay>
      <KeyEvent>
        <Makecode>54</Makecode>
      </KeyEvent>
    </MacroEvent>
    <MacroEvent>
      <Type>1</Type>
      <Delay>{self.delay}</Delay>
      <KeyEvent>
        <Makecode>{Keybord_to_numbers.keys_to_razer_numbers[line.lower()]}</Makecode>
      </KeyEvent>
    </MacroEvent>
    <MacroEvent>
      <Type>1</Type>
      <Delay>{self.delay}</Delay>
      <KeyEvent>
        <Makecode>{Keybord_to_numbers.keys_to_razer_numbers[line.lower()]}</Makecode>
        <State>1</State>
      </KeyEvent>
    </MacroEvent>
    <MacroEvent>
      <Type>1</Type>
      <Delay>{self.delay}</Delay>
      <KeyEvent>
        <Makecode>54</Makecode>
        <State>1</State>
      </KeyEvent>
    </MacroEvent>  
        """)

    def not_upper(self, line):
        print(False)
        self.new_file.write(f"""
             <MacroEvent>
              <Type>1</Type>
                <Delay>{self.delay}</Delay>
              <KeyEvent>
                <Makecode>{Keybord_to_numbers.keys_to_razer_numbers[line.lower()]}</Makecode>
              </KeyEvent>
            </MacroEvent>
            <MacroEvent>
              <Type>1</Type>
              <Delay>{self.delay}</Delay>
              <KeyEvent>
                <Makecode>{Keybord_to_numbers.keys_to_razer_numbers[line.lower()]}</Makecode>
                <State>1</State>
              </KeyEvent>
            </MacroEvent>           
        """)
