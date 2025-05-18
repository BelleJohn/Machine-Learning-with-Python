### 🔧 What is Model Merging?

**Model Merging** is a technique that allows you to combine the capabilities of different fine-tuned models—without requiring additional training or access to the original training data.

### 🧠 The Concept of Task Vectors

At the core of Model Merging lies the idea of the **Task Vector**. A Task Vector represents the capabilities that a fine-tuned model has learned beyond the base (foundation) model. Technically, it's the difference between the parameters (θ) of the fine-tuned model and those of the base model. You can think of these parameters as high-dimensional vectors.

### ⚙️ How Model Merging Works

Model Merging involves **adding the Task Vector of one model** to another model that has also been fine-tuned from the same foundation model. This approach may seem counterintuitive, as neural network parameters aren't typically treated as directly additive. However, research has shown that Task Vectors can, in fact, be added or subtracted with meaningful results.

### ✅ Key Requirement

The essential requirement for Model Merging to work is that all participating models must have been fine-tuned from the **same foundation model** and share the same network architecture. Thanks to the rise of well-known foundation models like **LLaMA**, this technique has become increasingly practical.

---

### 💡 Applications of Model Merging

* **Capability Addition**
  By adding Task Vectors that represent different skills, you can create a model that possesses multiple abilities. For example, combining a Chinese language Task Vector with a safety alignment Task Vector can yield a model that responds in Chinese while maintaining safe outputs. This technique has proven to be effective across different models (e.g., LLaMA, Mistral), languages (Chinese, Korean, Japanese), and tasks (reward modeling, coding, image interpretation). Weighting the Task Vectors (with factors like α, β) can further optimize results.

* **Capability Subtraction (Machine Unlearning)**
  Subtracting a Task Vector allows the model to "forget" a particular skill. This process is also known as **Machine Unlearning**. For example, subtracting a profanity Task Vector can remove the model’s ability to generate offensive language or even understand sensitive terms.

* **Analogy Transfer**
  Through analogical relationships (e.g., A is to B as C is to D), Task Vectors can be manipulated to help a model learn a new task **without access to data from the new task**. For instance, by analyzing differences between synthetic and real speech data in a general domain, you can adapt a model trained on synthetic data to perform as if it were trained on real data in a specific domain—effectively reducing speech recognition errors.

---

### ⚠️ Challenges and Influencing Factors

* Model Merging doesn’t always succeed. Simply adding Task Vectors may not yield optimal outcomes.
* A critical success factor is whether the parameter changes from different tasks **overlap**. When tasks modify **non-overlapping** parameters, merging is more likely to succeed.
* Research is ongoing to develop methods like **DeLoRA** and **TIES**, which reduce the number of parameters modified during fine-tuning, thereby improving merging success rates.
* **Model size** matters. Larger models tend to yield better results with merging, likely because they can assign different functions to different neurons or parameters, minimizing interference.

---

### 🔮 Future Outlook

Model Merging is an emerging field with many exciting directions for future research—especially in ensuring reliable and stable merging. A potential future development is the creation of a **Task Vector marketplace**, where users can "equip" their foundation models with various skills, much like equipping characters in a game. This would empower small teams to focus on developing individual Task Vectors and **share capabilities without sharing sensitive training data**. Since Model Merging involves only parameter arithmetic, it also requires **minimal computational resources**.

---

📺 **Reference:**
This summary is based on a YouTube video titled **「【生成式AI時代下的機器學習(2025)】第十一講：今天你想為 Foundation Model 裝備哪些 Task Vector？淺談神奇的 Model Merging 技術」**:
> *Note: The video is in Mandarin.*
🔗 [Watch here](https://www.youtube.com/watch?v=jFUwoCkdqAo&list=WL&index=3)



