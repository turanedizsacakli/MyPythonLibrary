from winotify import Notification , audio
import time as t
import winsound
#frequency
f=3799
#time
d=5000

t.sleep(2)
toast = Notification(
    app_id="be carreful turan...", 
    title="follow directions", 
    #msg="push there...",
    duration="short",#uyarı süresi
    icon=r"c:\path\to\icon.png")

toast.add_actions(label="push",
                launch="github.com/turanedizsacakli")
toast.set_audio(audio.Reminder, loop=False)

toast.show()
#winsound.Beep(f, d)
winsound.MessageBeep()




