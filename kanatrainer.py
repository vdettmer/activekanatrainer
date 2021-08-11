import random
import PySimpleGUI as sg # tested with 4.45.0 / use PySimpleGUIQt for macOS

dicthiragana = {'a':  'あ',      'i':     'い',      'u':     'う',      'e':    'え',      'o':  'お',
                'ka': 'か',      'ki':    'き',      'ku':    'く',      'ke':   'け',      'ko': 'こ',
                'sa': 'さ',      'shi':   'し',      'su':    'す',      'se':   'せ',      'so': 'そ',
                'ta': 'た',      'chi':   'ち',      'tsu':   'つ',      'te':   'て',      'to': 'と',
                'na': 'な',      'ni':    'に',      'nu':    'ぬ',      'ne':   'ね',      'no': 'の',
                'ha': 'は',      'hi':    'ひ',      'fu':    'ふ',      'he':   'へ',      'ho': 'ほ',
                'ma': 'ま',      'mi':    'み',      'mu':    'む',      'me':   'め',      'mo': 'も',
                'ya': 'や',      'yu':    'ゆ',      'yo':    'よ',
                'ra': 'ら',      'ri':    'り',      'ru':    'る',      're':   'れ',      'ro': 'ろ',
                'wa': 'わ',      'wo':    'を',
                'n':  'ん',
                'ga': 'が',      'gi':    'ぎ',      'gu':    'ぐ',      'ge':   'げ',      'go': 'ご',
                'za': 'ざ',      'ji':    'じ',      'zu':    'ず',      'ze':   'ぜ',      'zo': 'ぞ',
                'da': 'だ',      '(d)ji': 'ぢ',      '(d)zu': 'づ',      'de':   'で',      'do': 'ど',
                'ba': 'ば',      'bi':    'び',      'bu':    'ぶ',      'be':   'べ',      'bo': 'ぼ',
                'pa': 'ぱ',      'pi':    'ぴ',      'pu':    'ぷ',      'pe':   'ぺ',      'po': 'ぽ'}

dictkatakana = {'a':  'ア',      'i':     'イ',      'u':     'ウ',      'e':    'エ',      'o':  'オ',
                'ka': 'カ',      'ki':    'キ',      'ku':    'ク',      'ke':   'ケ',      'ko': 'コ',
                'sa': 'サ',      'shi':   'シ',      'su':    'ス',      'se':   'セ',      'so': 'ソ',
                'ta': 'タ',      'chi':   'チ',      'tsu':   'ツ',      'te':   'テ',      'to': 'ト',
                'na': 'ナ',      'ni':    'ニ',      'nu':    'ヌ',      'ne':   'ネ',      'no': 'ノ',
                'ha': 'ハ',      'hi':    'ヒ',      'fu':    'フ',      'he':   'ヘ',      'ho': 'ホ',
                'ma': 'マ',      'mi':    'ミ',      'mu':    'ム',      'me':   'メ',      'mo': 'モ',
                'ya': 'ヤ',      'yu':    'ユ',      'yo':    'ヨ',
                'ra': 'ラ',      'ri':    'リ',      'ru':    'ル',      're':   'レ',      'ro': 'ロ',
                'wa': 'ワ',      'wo':    'ヲ',
                'n':  'ン',
                'ga': 'ガ',      'gi':    'ギ',      'gu':    'グ',      'ge':   'ゲ',      'go': 'ゴ',
                'za': 'ザ',      'ji':    'ジ',      'zu':    'ズ',      'ze':   'ゼ',      'zo': 'ゾ',
                'da': 'ダ',      '(d)ji': 'ヂ',      '(d)zu': 'ヅ',      'de':   'デ',      'do': 'ド',
                'ba': 'バ',      'bi':    'ビ',      'bu':    'ブ',      'be':   'ベ',      'bo': 'ボ',
                'pa': 'パ',      'pi':    'ピ',      'pu':    'プ',      'pe':   'ペ',      'po': 'ポ'}

# initial Default
dictkana = dicthiragana
questionbit = "Hiragana"

def setKanaMode(kanaMode):
    global dictkana
    global kanakey
    global questionbit
    if kanaMode == "Hiragana":
        dictkana = dicthiragana
        kanakey = hiraganakey
        questionbit = "Hiragana"
    elif kanaMode == "Katakana":
        dictkana = dictkatakana
        kanakey = katakanakey
        questionbit = "Katakana"
    elif kanaMode == "Mixed":
        setKanaMixed()
    return questionbit

def setKanaMixed():
    global dictkana
    global kanakey
    global questionbit
    mode = random.randrange(0, 2)
    if mode == 0:
        dictkana = dicthiragana
        kanakey = hiraganakey
        questionbit = "Hiragana"
    else:
        dictkana = dictkatakana
        kanakey = katakanakey
        questionbit = "Katakana"
    return questionbit

if __name__ == '__main__':
    hiraganakey = random.choice(list(dicthiragana.keys()))
    # Set Default
    kanakey = hiraganakey
    katakanakey = random.choice(list(dictkatakana.keys()))

    # Define the window's contents
    layout = [[sg.Text(size=(25, 1), font=("Arial", 15), key='-QUESTION-', text='Write down Hiragana for '+kanakey)],
              [sg.Text(size=(10, 1), font=("Arial", 40), key='-OUTPUT-')],
              [sg.Button('Display Answer'), sg.Button('Next Kana'), sg.Button('Quit')],
              [sg.Radio('Hiragana', "MODE", default=True, size=(10, 1), key="-MODEHIRA-"), sg.Radio('Katakana', "MODE", key="-MODEKATA-"), sg.Radio('Mixed', "MODE")]]
    # Create the window
    window = sg.Window('Kana-Trainer 1.0', layout)

    # Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()
        if event == 'MODE':
            print("Hiragana")
        window['-QUESTION-'].update('Write down ' + questionbit + ' for '+kanakey)
        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
        # Output a message to the window
        elif event == 'Display Answer':
            window['-OUTPUT-'].update(dictkana[kanakey])
        elif event == 'Next Kana':
            if values["-MODEHIRA-"] == True:
                setKanaMode("Hiragana")
            elif values["-MODEKATA-"] == True:
                setKanaMode("Katakana")
            else:
                setKanaMode("Mixed")
            kanakey = random.choice(list(dictkana.keys()))
            window['-QUESTION-'].update('Write down ' + questionbit + ' for ' + kanakey)
            window['-OUTPUT-'].update('')
    window.close()
