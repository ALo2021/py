from pywinauto import Application

# ini notepad
app = Application().start("notepad.exe")

# escrever
notepad = app.window(title_re=".*Notepad")
notepad.type_keys("Teste automação", with_spaces=True)

# fechar s/ salvar
notepad.menu_select("File -> Exit")
app.window(title_re=".*Notepad").window(title_re=".*Notepad").child_window(title="Don't Save").click()
