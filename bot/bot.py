import discord
from transformers import VitsModel, AutoTokenizer
import torch
import scipy.io.wavfile as wavfile

# Discord 봇 설정
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# 파인튜닝된 모델 로드
model = VitsModel.from_pretrained("models/fine_tuned_model/")
tokenizer = AutoTokenizer.from_pretrained("models/fine_tuned_model/")

# 음성 생성 함수
def generate_speech(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True)
    with torch.no_grad():
        output = model(**inputs).waveform.squeeze().numpy()
    wavfile.write("output.wav", rate=22050, data=output)
    return "output.wav"

# Discord 봇 이벤트 처리
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.content.startswith("!tts"):
        text = message.content[len("!tts "):]
        audio_file = generate_speech(text)

        if message.author.voice:  # 음성 채널에 사용자가 있는 경우
            voice_channel = message.author.voice.channel
            vc = await voice_channel.connect()
            vc.play(discord.FFmpegPCMAudio(audio_file))
            while vc.is_playing():
                await discord.utils.sleep_until(0.1)
            await vc.disconnect()

# 봇 실행
client.run()    # 디스코드 봇 토큰 입력
