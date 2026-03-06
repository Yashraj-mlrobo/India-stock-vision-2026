import numpy as np
import pandas as pd
from tensorflow.keras.callbacks import EarlyStopping
from src.model_trainer import build_lstm_model

def start_training(x_train, y_train):
    # 1. Define the model architecture from our src folder
    model = build_lstm_model((x_train.shape[1], 1))
    
    # 2. Early Stopping: Stop training if the loss stops improving
    # This prevents the model from 'overfitting' to the NSE data
    early_stop = EarlyStopping(monitor='loss', patience=5, restore_best_weights=True)
    
    # 3. The Training Loop
    print("Starting Nifty 50 Model Training...")
    history = model.fit(
        x_train, y_train, 
        epochs=50, 
        batch_size=32, 
        callbacks=[early_stop],
        verbose=1
    )
    
    # 4. Save the trained weights
    model.save('training/nifty_lstm_v1.h5')
    print("Model saved to training/nifty_lstm_v1.h5")
    return history

if __name__ == "__main__":
    print("Training script ready.")
