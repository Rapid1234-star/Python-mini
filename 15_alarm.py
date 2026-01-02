# Python Alarm Clock (with seconds)
import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"\n⏰ Alarm set for {alarm_time}\n")

    sound_file = "treachery.mp3"  # Ensure this file exists
    pygame.mixer.init()

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Current time: {current_time}", end="\r")

        if current_time == alarm_time:
            print("\n\n🔔 Wake up! Alarm ringing!\n")
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            break

        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)
