import yt_dlp
import os
import subprocess

base_dir = os.path.abspath("./DiscordTTSBotRaccoon/TTS-0.13.1/DataSet")
wav_directory = os.path.join(base_dir, "wavs")

# 1. 유튜브 링크 및 출력 파일 설정
youtube_link = "https://youtu.be/OqJ0MJNgr-M?si=BeSb4Qfe6HxilbC7"
output_dir = wav_directory  # 파일을 저장할 디렉토리
filename = "audio"  # 기본 파일명

# yt-dlp 옵션 설정
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(output_dir, filename),  # 확장자 없이 파일명만 지정
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
}

# 2. 유튜브 제목 가져오기 및 파일명 생성
with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
    info_dict = ydl.extract_info(youtube_link, download=False)
    video_title = info_dict.get('title', 'audio').replace(" ", "_").replace("/", "_").replace("'", "").replace("(", "").replace(")", "")

output_wav = os.path.join(output_dir, video_title + ".wav")

# 3. 기존 파일 확인
if not os.path.isfile(output_wav):
    # 파일이 없는 경우 다운로드
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_link])
    
    # 다운로드된 파일 찾기
    downloaded_files = os.listdir(output_dir)
    downloaded_wav = None
    
    for file in downloaded_files:
        if file.endswith(".wav") and file.startswith(filename):
            downloaded_wav = os.path.join(output_dir, file)
            break

    if downloaded_wav and os.path.isfile(downloaded_wav):
        # 다운로드된 파일을 모노로 변환하여 저장
        subprocess.run([
            'ffmpeg', '-i', downloaded_wav, '-ac', '1', output_wav
        ])
        print(f"파일이 성공적으로 모노로 변환되어 생성되었습니다: {output_wav}")
    else:
        print(f"다운로드된 .wav 파일을 찾을 수 없습니다: {output_dir}")
else:
    print(f"기존 파일 {output_wav}을(를) 사용합니다.")

# 4. 추출된 오디오 파일에서 구간을 추출하여 새로운 WAV 파일로 저장
start_time = ""
end_time = ""
output_segment = os.path.join(output_dir, "segment_174.wav")

# ffmpeg 명령어 실행
subprocess.run([
    'ffmpeg', '-i', output_wav, '-ss', start_time, '-to', end_time, '-c', 'copy', output_segment
])

if os.path.isfile(output_segment):
    print(f"{output_segment} 생성 완료.")
else:
    print(f"{output_segment} 생성에 실패했습니다.")




