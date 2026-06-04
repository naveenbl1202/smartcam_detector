"""
Smart Camera Object Detector
----------------------------
Ett litet datorseende-program som hittar och raknar objekt och personer i en bild –
samma typ av video-analys som korr direkt pa en Axis-kamera (edge analytics).

Anvander en fardigtranad YOLOv8-modell (du tranar alltsa ingen modell sjalv – du
anvander en redan tranad, precis som analysen som korr pa en kameras chip).

Korning:
    python object_detector.py --image min_bild.jpg

Output:
    - en ny bild "output.jpg" med rutor runt varje hittat objekt
    - en utskrift med antal personer och objekt
    - ett "INTRANGSLARM" om minst en person upptacks (sakerhets-touch)
"""
import argparse
from ultralytics import YOLO
import cv2


def detect(image_path: str, model_name: str = "yolov8n.pt", output_path: str = "output.jpg"):
    # 1. Ladda den fardigtranade modellen (laddas ner forsta gangen)
    model = YOLO(model_name)

    # 2. Kor detektion pa bilden
    results = model(image_path)
    result = results[0]

    # 3. Rita rutor runt allt som hittades och spara bilden
    annotated = result.plot()          # numpy-bild med rutor (BGR)
    cv2.imwrite(output_path, annotated)

    # 4. Rakna vad som hittades
    names = model.names                # t.ex. {0: 'person', 2: 'car', ...}
    classes = [int(c) for c in result.boxes.cls.tolist()]
    counts = {}
    for c in classes:
        label = names[c]
        counts[label] = counts.get(label, 0) + 1

    # 5. Skriv ut resultatet
    print(f"\nHittade {len(classes)} objekt i '{image_path}':")
    for label, n in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"  - {label}: {n}")
    print(f"\nSparade resultatbild: {output_path}")

    # 6. Enkel sakerhetsfunktion: larma om en person syns
    people = counts.get("person", 0)
    if people > 0:
        print(f"\n  INTRANGSLARM: {people} person(er) upptackt(a) i bilden!")
    else:
        print("\nOK: inga personer upptackta.")

    return counts


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Smart Camera Object Detector")
    parser.add_argument("--image", required=True, help="Sokvag till bilden som ska analyseras")
    parser.add_argument("--model", default="yolov8n.pt", help="YOLO-modell (default: yolov8n.pt)")
    parser.add_argument("--output", default="output.jpg", help="Filnamn for resultatbilden")
    args = parser.parse_args()
    detect(args.image, args.model, args.output)
