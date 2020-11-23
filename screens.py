import mido, lpxPads as pads, config;

def setScreen(lpx, outports, screen):
    global submenu

    # Set initial submenu
    if screen == 'notes':
        submenu = 'edo'
    elif screen == 'settings':
        submenu = 'settings-1'

    initSubmenu(lpx)
    
    # Listen to notes
    for msg in lpx:
        if msg.type == "control_change":
            if msg.value == 0:
                # Menu back
                if msg.control == pads.menu[screen]['note']:
                    return 'edo'
                
                # Submenu 1
                elif msg.control == pads.xy_to_pad_note([8, 7]):
                    if screen == 'notes' and submenu != 'edo':
                        submenu = 'edo'
                        initSubmenu(lpx)
                        
                # Submenu 2
                elif msg.control == pads.xy_to_pad_note([8, 6]):
                    if screen == 'notes' and submenu != 'row':
                        submenu = 'row'
                        initSubmenu(lpx)
                        
        elif msg.type == 'note_on' and msg.velocity > 2:
            xy = pads.pad_note_to_xy(msg.note)
            edo = 1 + xy[0] + 8*(7-xy[1])
            pads.display_text(lpx, str(edo), False)
            config.set('edo', edo)
            displayEdoPads(lpx)
            

def initSubmenu(lpx):
    # Reset
    pads.display_reset(lpx, False)

    # Display menu glow + set submenu
    if screen == 'notes':
        pads.display_menu_glow(lpx, pads.menu['notes']['xy'])
    elif screen == 'settings':
        pads.display_menu_glow(lpx, pads.menu['settings']['xy'])
        
    if submenu == 'edo':
        pads.display_text(lpx, 'EDO', False)
        displayEdoSubmenu(lpx)
        displayEdoPads(lpx)
    elif submenu == 'row':
        pads.display_text(lpx, 'ROW', False)
        displayEdoSubmenu(lpx)

def displayEdoSubmenu(lpx):
    rgb_low  = [0.05, 0.15, 0.05]
    rgb_high = [0.60, 1.00, 0.60]
    pads.display_multi(lpx, [
        [[8,7], rgb_high if submenu == 'edo' else rgb_low],   # Submenu edo
        [[8,6], rgb_high if submenu == 'row' else rgb_low],   # Submenu row
    ])

def displayEdoPads(lpx):
    rgb_low  = [0.2, 0.2, 0.2]
    rgb_high = [1.0, 1.0, 1.0]
    rgb_12   = [0.2, 0.1, 0.3]
    rgb_12h  = [0.8, 0.2, 1.0]
    pads.display_multi(lpx, [
        [[0,7], rgb_high if config.get('edo')==1  else rgb_low],   # EDO 01
        [[1,7], rgb_high if config.get('edo')==2  else rgb_low],   # EDO 02
        [[2,7], rgb_high if config.get('edo')==3  else rgb_low],   # EDO 03
        [[3,7], rgb_high if config.get('edo')==4  else rgb_low],   # EDO 04
        [[4,7], rgb_high if config.get('edo')==5  else rgb_low],   # EDO 05
        [[5,7], rgb_high if config.get('edo')==6  else rgb_low],   # EDO 06
        [[6,7], rgb_high if config.get('edo')==7  else rgb_low],   # EDO 07
        [[7,7], rgb_high if config.get('edo')==8  else rgb_low],   # EDO 08
        [[0,6], rgb_high if config.get('edo')==9  else rgb_low],   # EDO 09
        [[1,6], rgb_high if config.get('edo')==10 else rgb_low],   # EDO 10
        [[2,6], rgb_high if config.get('edo')==11 else rgb_low],   # EDO 11
        [[3,6], rgb_12h  if config.get('edo')==12 else rgb_12 ],   # EDO 12
        [[4,6], rgb_high if config.get('edo')==13 else rgb_low],   # EDO 13
        [[5,6], rgb_high if config.get('edo')==14 else rgb_low],   # EDO 14
        [[6,6], rgb_high if config.get('edo')==15 else rgb_low],   # EDO 15
        [[7,6], rgb_high if config.get('edo')==16 else rgb_low],   # EDO 16
        [[0,5], rgb_high if config.get('edo')==17 else rgb_low],   # EDO 17
        [[1,5], rgb_high if config.get('edo')==18 else rgb_low],   # EDO 18
        [[2,5], rgb_high if config.get('edo')==19 else rgb_low],   # EDO 19
        [[3,5], rgb_high if config.get('edo')==20 else rgb_low],   # EDO 20
        [[4,5], rgb_high if config.get('edo')==21 else rgb_low],   # EDO 21
        [[5,5], rgb_high if config.get('edo')==22 else rgb_low],   # EDO 22
        [[6,5], rgb_high if config.get('edo')==23 else rgb_low],   # EDO 23
        [[7,5], rgb_high if config.get('edo')==24 else rgb_low],   # EDO 24
        [[0,4], rgb_high if config.get('edo')==25 else rgb_low],   # EDO 25
        [[1,4], rgb_high if config.get('edo')==26 else rgb_low],   # EDO 26
        [[2,4], rgb_high if config.get('edo')==27 else rgb_low],   # EDO 27
        [[3,4], rgb_high if config.get('edo')==28 else rgb_low],   # EDO 28
        [[4,4], rgb_high if config.get('edo')==29 else rgb_low],   # EDO 29
        [[5,4], rgb_high if config.get('edo')==30 else rgb_low],   # EDO 30
        [[6,4], rgb_high if config.get('edo')==31 else rgb_low],   # EDO 31
        [[7,4], rgb_high if config.get('edo')==32 else rgb_low],   # EDO 32
        [[0,3], rgb_high if config.get('edo')==33 else rgb_low],   # EDO 33
        [[1,3], rgb_high if config.get('edo')==34 else rgb_low],   # EDO 34
        [[2,3], rgb_high if config.get('edo')==35 else rgb_low],   # EDO 35
        [[3,3], rgb_high if config.get('edo')==36 else rgb_low],   # EDO 36
        [[4,3], rgb_high if config.get('edo')==37 else rgb_low],   # EDO 37
        [[5,3], rgb_high if config.get('edo')==38 else rgb_low],   # EDO 38
        [[6,3], rgb_high if config.get('edo')==39 else rgb_low],   # EDO 39
        [[7,3], rgb_high if config.get('edo')==40 else rgb_low],   # EDO 40
        [[0,2], rgb_high if config.get('edo')==41 else rgb_low],   # EDO 41
        [[1,2], rgb_high if config.get('edo')==42 else rgb_low],   # EDO 42
        [[2,2], rgb_high if config.get('edo')==43 else rgb_low],   # EDO 43
        [[3,2], rgb_high if config.get('edo')==44 else rgb_low],   # EDO 44
        [[4,2], rgb_high if config.get('edo')==45 else rgb_low],   # EDO 45
        [[5,2], rgb_high if config.get('edo')==46 else rgb_low],   # EDO 46
        [[6,2], rgb_high if config.get('edo')==47 else rgb_low],   # EDO 47
        [[7,2], rgb_high if config.get('edo')==48 else rgb_low],   # EDO 48
        [[0,1], rgb_high if config.get('edo')==49 else rgb_low],   # EDO 49
        [[1,1], rgb_high if config.get('edo')==50 else rgb_low],   # EDO 50
        [[2,1], rgb_high if config.get('edo')==51 else rgb_low],   # EDO 51
        [[3,1], rgb_high if config.get('edo')==52 else rgb_low],   # EDO 52
        [[4,1], rgb_high if config.get('edo')==53 else rgb_low],   # EDO 53
        [[5,1], rgb_high if config.get('edo')==54 else rgb_low],   # EDO 54
        [[6,1], rgb_high if config.get('edo')==55 else rgb_low],   # EDO 55
        [[7,1], rgb_high if config.get('edo')==56 else rgb_low],   # EDO 56
        [[0,0], rgb_high if config.get('edo')==57 else rgb_low],   # EDO 57
        [[1,0], rgb_high if config.get('edo')==58 else rgb_low],   # EDO 58
        [[2,0], rgb_high if config.get('edo')==59 else rgb_low],   # EDO 59
        [[3,0], rgb_high if config.get('edo')==60 else rgb_low],   # EDO 60
        [[4,0], rgb_high if config.get('edo')==61 else rgb_low],   # EDO 61
        [[5,0], rgb_high if config.get('edo')==62 else rgb_low],   # EDO 62
        [[6,0], rgb_high if config.get('edo')==63 else rgb_low],   # EDO 63
        [[7,0], rgb_high if config.get('edo')==64 else rgb_low],   # EDO 64
    ])
        
