import openai 

openai.api_key = "sk-proj-eRtVPpgNx8Jmq031aM2wT3BlbkFJZoJr8eqjGCEqUNjsQkhy"
def classify_packet_with_gpt(packet_features):
    prompt = f"Classify the following network packet as normal, suspicious, or malicious:\n{packet_features}"
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can use the model of your choice, e.g., "text-davinci-003"
            prompt=prompt,
            max_tokens=10,
            n=1,
            stop=None,
            temperature=0.5
        )
        # Parse the response
        result = response.choices[0].text.strip().lower()
        return result
    except Exception as e:
        return f"Error with GPT: {str(e)}"