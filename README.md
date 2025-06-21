# AutoCreator v1

**Version**: 1.0
**Status**: Completed core pipeline ✅
**Author**: Shashwat Patkar
**Goal**: Fully local, free, automated YouTube video generator and uploader using AI.

---

## 🚀 What is AutoCreator?

AutoCreator is a zero-cost, fully offline YouTube content generation pipeline. It:

* 🎯 Uses Ollama + Mistral to generate **content ideas** based on YouTube trends.
* 🧠 Generates a **script** using local LLM.
* 🗣️ Converts text to **speech** using `pyttsx3`.
* 🖼️ Finds relevant **images** via Bing image downloader.
* 🎞️ Uses FFmpeg to create a **still image video**.
* ⬆️ Optionally uploads the video to YouTube.
* 📊 Logs data and marks used ideas in `data.xlsx`.

---

## 📁 Folder Structure

```
autocreator/
├── idea_gen.py               # Fetch and mark content ideas
├── generate_audio.py         # TTS generation
├── generate_image.py         # Image download via Bing
├── generate_video.py         # FFmpeg video generator
├── upload_video.py           # YouTube uploader (OAuth)
├── run_pipeline.py           # Main orchestrator script
├── run_full_pipeline.ps1     # PowerShell runner for pipeline
├── create_run_pipeline.ps1   # One-time script creator
├── media/                    # Generated media: audio, image, video
├── data.xlsx                 # Tracks ideas and their usage
├── improvements.xlsx         # (Planned) Log enhancement ideas
└── .gitignore                # Git exclusions
```

---

## 🧠 Python Files Description

| File                      | Purpose                                                                 |
| ------------------------- | ----------------------------------------------------------------------- |
| `idea_gen.py`             | Uses Ollama + Mistral to generate a topic + script and logs it in Excel |
| `generate_audio.py`       | Converts script into MP3 using pyttsx3 + pydub                          |
| `generate_image.py`       | Downloads a relevant image from Bing based on idea                      |
| `generate_video.py`       | Creates a static video using FFmpeg from image/audio                    |
| `upload_video.py`         | Uploads final video and thumbnail to YouTube                            |
| `run_pipeline.py`         | Coordinates all steps into one pipeline                                 |
| `run_full_pipeline.ps1`   | PowerShell wrapper to activate venv + run the pipeline                  |
| `create_run_pipeline.ps1` | Initializes the runner script                                           |

---

## 📝 How to Run

1. Setup `venv`, install dependencies (`requirements.txt`)
2. Run `run_full_pipeline.ps1` to generate a full video
3. Auto upload to YouTube (if enabled)

---

## 📈 What's Working?

* ✅ Fully working AI pipeline
* ✅ Local LLM usage with Mistral
* ✅ Free tools only (no paid APIs)
* ✅ Basic YouTube uploader
* ✅ GitHub-safe files committed

---

## 🔧 Future Enhancements

* [ ] Improved image relevance using enhanced prompt chaining
* [ ] Optionally generate animated video with captions
* [ ] Use Whisper for automatic subtitles
* [ ] Add video queue support
* [ ] Modular configuration system

---

## 📜 License

MIT License (you can freely use and extend)

---

## 🙌 Special Thanks

* OpenAI (ChatGPT guidance)
* Mistral AI (local LLM)
* ffmpeg.org
* pyttsx3 + pydub
* Google APIs
* GitHub Copilot

---

### 📌 Contact

For feedback or contributions: [patkars69](https://github.com/patkars69)
