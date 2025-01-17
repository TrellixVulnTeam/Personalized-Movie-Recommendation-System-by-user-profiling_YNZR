def select_emoticon(x):
    return {
        ":)"  : 'happy',
        ":("  : 'sad',
        ":o"  : 'surprised',
        ":-*" : 'kizz',
        ":-D" : 'laugh',
        ">:-o": 'angry',
        "=D>" : 'applause',
        ">:D<": 'hug',
        ":-\\": 'undecided',
        ":-|" : 'whatever',
        ";-)" : 'wink',
        "8-)" : 'cool',
        ":'(" : 'cry',
        "<:-|": 'foolish',
        ":-!" : 'foot in mouth',
        "X;{" : 'sick',
        "<3"  : 'love',
        "(y)" : 'good',
        ":D"  : 'laugh',
        ";)"  : 'wink',
        ":/"  : 'confused',
        "|‑O" : 'bored',
        ":‑ /": 'disappointed',
        "d;"  : 'disgust',
        "% ‑)": 'drunk',
        ":$"  : 'embarrassed',
        ":'‑)": 'emotional',
        ">:‑)": 'evil',
        ">:/" : 'hesitant',
        "d: <": 'horror',
        "O:‑)": 'innocent',
        ":‑p" : 'playful',
        "*-)" :'smirk'
    }.get(x, x)