[reflection.md](https://github.com/user-attachments/files/33719133/reflection.md)
# Reflection — Module 5

On the Module 4 IMDB movie review classifier, validation loss hit its lowest
point around epoch 3, then climbed steadily for the rest of the 20-epoch run
while training accuracy kept climbing toward 100% — a clear sign of
overfitting. I caught it, retrained a fresh model for 4 epochs instead of 20,
and got 87.85% test accuracy. So the step I stopped on was "identify the
turnaround epoch and retrain" — right where the workflow says to stop
scaling once validation performance turns.

This time, with the Steam Gap Analyzer, I'm starting from a working data
pipeline (fetch, clean, enrich) and a simple heuristic (genre count
quantiles) instead of a trained model. The new part for me is adding an
actual Keras model with a real evaluation protocol — right now the "gap"
signal is just low game count, and I want to combine that with a predicted-
interest signal (e.g. predicted metacritic score) so the gaps are more
meaningful than just "nobody's made this yet."
