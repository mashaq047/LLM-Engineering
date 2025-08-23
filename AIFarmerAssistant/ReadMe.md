
## AI Farming Advisor (LLM + Quantization + Edge Deployment)

#### 📌 Overview
This project demonstrates how to **run a quantized Large Language Model (LLM) on resource-constrained devices** such as laptops, smartphones, or small edge devices.  
It uses the **Microsoft Phi-3 Mini Instruct** model with **8-bit quantization** (via `bitsandbytes`) to make inference lighter and faster, while maintaining useful performance.  

The chatbot is designed as an **AI Farming Advisor** that can give contextual answers, enhanced by **real-time location and weather data**.  

---

#### 🎯 Key Features
- ✅ **Quantization (8-bit)** for optimized model loading on GPUs/CPUs with graceful fallbacks  
- ✅ **Custom System Prompt** → “AI Farming Advisor”  
- ✅ **Context Integration** → Uses IP-based location + OpenWeatherMap API for real-time weather info  
- ✅ **Streaming Chat UI** → Built with **Gradio** for a responsive chatbot experience  
- ✅ **Lightweight Deployment** → Potential to run on smaller devices (edge AI vision)  

---

#### ⚙️ Tech Stack
- [Transformers](https://huggingface.co/docs/transformers) – Model loading & inference  
- [Bitsandbytes](https://github.com/TimDettmers/bitsandbytes) – 8-bit quantization  
- [Torch](https://pytorch.org/) – Model execution (GPU/CPU)  
- [Gradio](https://gradio.app/) – Interactive chatbot UI  
- [Geocoder](https://geocoder.readthedocs.io/) – Location detection  
- [OpenWeatherMap API](https://openweathermap.org/api) – Weather integration  

---

#### 🚀 Pipeline
1. **Install Dependencies**  
   ```bash
   pip install torch transformers accelerate bitsandbytes gradio sentencepiece requests geocoder
```