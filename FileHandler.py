import Keybord_to_numbers


class FileHandler:

    def __init__(self,
                 file_loc="C:\\Users\\danie\\Desktop\\Macro_thing\\input.txt",
                 new_file_loc="C:\\Users\\danie\\Desktop\\Macro_thing\\Macro 2.xml"):
        self.file = open(file_loc, "r")
        self.new_file = open(new_file_loc, "w")
        Keybord_to_numbers.keys_to_razer_numbers
        self.delay = 10

    def input_file(self):
        f = self.file.readline()

        # True While it is not at the end of the text document
        while f != "":
            # Iterate over index
            for element in range(0, len(f)):
                # convert letters to the razer numbers
                if f[element].isupper():
                    self.is_upper(f[element])
                else:
                    self.not_upper(f[element])
            f = self.file.readline()

    def file_header(self):
        self.new_file.write("""
<?xml version="1.0" encoding="utf-8"?>
<Macro xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <Name>Macro 1</Name>
  <Guid>a7bbbe84-49fc-482d-8895-43191603c068</Guid>
  <MacroEvents>
""".strip())

    def file_footer(self):
        self.new_file.write("""
  </MacroEvents>
  <IsFolder>false</IsFolder>
  <FolderGuid>00000000-0000-0000-0000-000000000000</FolderGuid>
</Macro>    
""")

    # if the chariter is upper case it sould go here to use the sift key
    def is_upper(self, line):
        print(False)
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
        print(True)
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
