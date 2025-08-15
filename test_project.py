#!/usr/bin/env python3
"""
Test script to verify the Stock Project structure and imports
"""

def test_imports():
    """Test if all modules can be imported successfully"""
    try:
        print("Testing imports...")
        
        # Test core modules
        import streamlit as st
        print("✅ Streamlit imported successfully")
        
        import pandas as pd
        print("✅ Pandas imported successfully")
        
        import numpy as np
        print("✅ NumPy imported successfully")
        
        import matplotlib.pyplot as plt
        print("✅ Matplotlib imported successfully")
        
        import yfinance as yf
        print("✅ YFinance imported successfully")
        
        # Test custom modules
        from config import stock_symbols
        print("✅ Config module imported successfully")
        
        from utils.data_fetcher import get_stock_data
        print("✅ Data fetcher module imported successfully")
        
        from utils.metrics_calculator import calculate_stock_metrics
        print("✅ Metrics calculator module imported successfully")
        
        from utils.arima_forecaster import ARIMAForecaster
        print("✅ ARIMA forecaster module imported successfully")
        
        from utils.lstm_forecaster import LSTMForecaster
        print("✅ LSTM forecaster module imported successfully")
        
        from utils.ui_components import create_header
        print("✅ UI components module imported successfully")
        
        print("\n🎉 All imports successful! Project structure is correct.")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def test_config():
    """Test configuration data"""
    try:
        print("\nTesting configuration...")
        
        from config import stock_symbols, APP_CONFIG, MODEL_CONFIG
        
        # Test stock symbols
        print(f"✅ Stock symbols loaded: {len(stock_symbols)} stocks")
        
        # Test app config
        print(f"✅ App config loaded: {APP_CONFIG['title']}")
        
        # Test model config
        print(f"✅ Model config loaded: ARIMA order {MODEL_CONFIG['arima']['order']}")
        
        return True
        
    except Exception as e:
        print(f"❌ Configuration error: {e}")
        return False

def test_utility_functions():
    """Test utility functions"""
    try:
        print("\nTesting utility functions...")
        
        from utils.data_fetcher import validate_stock_symbol
        from utils.metrics_calculator import calculate_stock_metrics
        
        # Test stock validation
        is_valid = validate_stock_symbol("TCS.NS")
        print(f"✅ Stock validation working: TCS.NS is {'valid' if is_valid else 'invalid'}")
        
        # Test metrics calculation with dummy data
        import pandas as pd
        dummy_data = pd.DataFrame({
            'Close': [100, 110, 105, 120, 95],
            'Volume': [1000, 1100, 1050, 1200, 950]
        })
        
        metrics = calculate_stock_metrics(dummy_data)
        print(f"✅ Metrics calculation working: {len(metrics)} metrics calculated")
        
        return True
        
    except Exception as e:
        print(f"❌ Utility functions error: {e}")
        return False

def main():
    """Main test function"""
    print("🚀 Stock Project - Structure Test")
    print("=" * 50)
    
    # Run all tests
    tests = [
        test_imports,
        test_config,
        test_utility_functions
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Project is ready to run.")
        print("\nTo run the application:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Run the app: streamlit run app.py")
    else:
        print("❌ Some tests failed. Please check the errors above.")
    
    return passed == total

if __name__ == "__main__":
    main() 