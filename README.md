# 🚧 Road Damage Severity Analyzer

An AI-powered web application that detects road damage from images and estimates its severity using computer vision and object detection.

## 📌 Project Overview

Road damage such as potholes and cracks can affect road safety and vehicle movement. Manually identifying and assessing road damage can be time-consuming.

The **Road Damage Severity Analyzer** provides an automated approach where a user uploads a road image and the system analyzes it to identify visible damage and estimate its severity.

## ✨ Features

- 🕳️ Road damage detection
- 🤖 YOLO-based object detection
- 📊 AI confidence score
- 📐 Estimated damaged area
- 🚦 Severity classification: LOW, MEDIUM, HIGH
- 📍 GPS-based location capture
- 🖼️ Road image upload and preview
- 🌐 Flask-based web interface

## 🔍 Damage Types

The prototype supports detection of road damage such as:

- Pothole
- Alligator crack
- Longitudinal crack
- Road patch

## ⚙️ How It Works

```text
User uploads road image
          ↓
GPS location captured
          ↓
Image processing
          ↓
YOLO object detection
          ↓
Damage type identified
          ↓
Damaged area estimated
          ↓
Severity score calculated
          ↓
Final analysis displayed
