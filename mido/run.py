import time, sched, mido
import xedo

# SETTINGS

# To know what is the midi identifier of your Launchpad X,
# plug it and use these lines:
# import mido
# mido.get_ioport_names()

# Note: the Launchpad X appears twice.
# Ignore the first instance, which is dedicated to the DAW.
# Use the second MIDI interface.

settings = {
    'launchpad_midi_id': 'Launchpad X:Launchpad X MIDI 2 24:1',
    'edo': 17,
    'row_offset': 7,
    'pitch_bend_range_semitones': 96,   # This must match the synth's settings
                                        # Modal Skulpt: 48
                                        # Continuumini: 96
    'root_note': 60 # 60 is the middle C    
}

s = sched.scheduler(time.time, time.sleep)

def testLPX(sc):
    global lpx
    if settings['launchpad_midi_id'] in mido.get_input_names():
        print("Launchpad X connected")
        with mido.open_ioport(settings['launchpad_midi_id']) as lpx:
            switchToProgrammerMode(lpx, False)
            print(settings['edo'], "EDO")
            xedo.xedo(settings)
    else:
        print("Waiting for Launchpad X...")
        s.enter(3, 1, testLPX, (sc,))

def switchToProgrammerMode(lpx, flag):
    # The reference is in the LPX programmer's manual
    # https://fael-downloads-prod.focusrite.com/customer/prod/s3fs-public/downloads/Launchpad%20X%20-%20Programmers%20Reference%20Manual.pdf
    if flag:
        switch = mido.Message.from_hex('F0 00 20 29 02 0C 0E 01 F7')
    else:
        switch = mido.Message.from_hex('F0 00 20 29 02 0C 0E 00 F7')
    lpx.send(switch)
    print("Launchpad X switched to programmer mode")
        
s.enter(0, 1, testLPX, (s,))
s.run()
