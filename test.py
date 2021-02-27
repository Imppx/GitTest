import time
import json


s = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'


print (len(s))

print("\n")

for i in range(0, 2):
    print("--\n")


print (str(int(time.time())))

print("Auto_test: " + str(int(time.time())) + 'a' * 128)


def get_millisecond_timestamp():
    return int(round(time.time() * 1000))

t = get_millisecond_timestamp()
t2 = t - (30 * 60 * 1000)

print(t, t2)

res = []
print(res == [])


data = {
        "method": "report",
        "clientToken": "8AY0ENTMBE-1",
        "params": {
            "dev_info": {
                "video_codec": "mp4",
                "audio_codec": "mp3"
            },
            "record_enable": 1,
            "_sys_xp2p_info": "test_video",
            "_sys_cs_days": 5,
            "_sys_cs_status": 0,
            "_sys_cs_type": 1,
            "position": "昆明"
        }
    }


print(json.dumps(data))

