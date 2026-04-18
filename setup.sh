#!/bin/bash

# IoT Dashboard Setup Script
# This script automates the setup process

echo "🚀 Setting up Universal IoT Dashboard..."
echo ""

# Check Python installation
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.7 or higher."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"

# Create virtual environment (optional but recommended)
read -p "Do you want to create a virtual environment? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    
    # Activate virtual environment
    if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
        source venv/Scripts/activate
    else
        source venv/bin/activate
    fi
    
    echo "✅ Virtual environment created and activated"
fi

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "✅ Setup complete!"
echo ""
echo "To run the dashboard:"
echo "  streamlit run app.py"
echo ""
echo "To run the simulator (in another terminal):"
echo "  python simulator.py"
echo ""
echo "Happy monitoring! 📊"
