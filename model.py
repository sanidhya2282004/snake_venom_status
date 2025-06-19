from fastai.vision.all import *
from PIL import Image
import warnings
warnings.filterwarnings('ignore')

# Load model
try:
    learn_inf = load_learner(r'c:\Users\HP\Snake\Snake-Classification\snake_predict.pkl')
    print("✅ Model loaded successfully.")
except Exception as e:
    print(f"❌ Failed to load model: {e}")
    learn_inf = None

def predict_snake(image_path):
    if learn_inf is None:
        return "Model not loaded"

    try:
        pil_img = Image.open(image_path).convert("RGB")
        img = PILImage.create(pil_img)

        pred, _, _ = learn_inf.predict(img)

        # Normalize to lowercase for comparison
        pred_lower = [str(p).lower() for p in pred]

        if "venomous" in pred_lower:
            return "venomous"
        elif "non venomous" in pred_lower or "non-venomous" in pred_lower:
            return "non-venomous"
        else:
            return "unknown"

    except Exception as e:
        return f"❌ Error: {e}"
