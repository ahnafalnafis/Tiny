from cx_Freeze import setup, Executable

setup(name="FRIDAY",
      version="1.40.2",
      author="Ahnaf Al Nafis",
      executables=[Executable(r"A:\Code\Tests\Python\ahnaf.py",
                              icon=r"A:\Icons\Jarvis-white.png",
                              shortcut_name="FRIDAY",
                              shortcutDir="DesktopFolder")]
      )
