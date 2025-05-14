PROMPT="Write an NHS doctor’s letter based on the following conversation between a patient and a doctor. End the letter with a clear action plan and follow information. It important to only use the information provided in the conversation:"

USER_input="""Write an NHS doctor’s letter based on the following conversation between a patient and a doctor. End the letter with a clear action plan and follow information. It important to only use the information provided in the conversation:
Hi, my name is Adam. I'm a doctor. I work in oncology. How can I help? Hello, doctor. I have pain in my tummy and I've been losing weight over the last three weeks. Oh, I'm sorry to hear that How long has this been his this issue been going on for? It's been going on for three and a half months now I'm sorry to hear that. Do you have any other symptoms? I have a bloating and I have loose stool. Oh, I'm sorry to hear that. Do you know how much weight you've lost over the last three and a half months? Well, I used to be 13 stone and now I'm 11 stone. Okay, and was that weight loss all intentional or not intentional? Have you been dieting at all? No, doctor, I haven't been dieting at all. It just lost I just lost this weight unintentionally. Okay, have you had any other symptoms such as vomiting, feeling sick or loss of appetite or tummy pain or passing blood in your stool or passing burning sensation when you pass water or anything else you haven't mentioned. Only loose stool Okay, and is your stool Is the color abnormal? The color is normal. Let's just watery and I go to the toilet twice a day. Okay, all right. Well, look There's a few things that are going through my head. It's unclear what's causing you these symptoms right now But what I want to do is I want to get a scan of your tummy to just to look at the your organs and make sure everything is okay there So we'll do a CT scan of the abdomen and pelvis and we might do a scan of the chest just just for completion We'll also need you to give us a sample of your stool so we can run a test on that So we'll do a stool analysis and I'll also do some blood tests including a full blood count a liver function test a urea and renal function test and we'll look at your calcium levels and we'll also Look at some other markers such as tumor markers Do you have any concerns at the moment? Well, doctor. I'm concerned that it's cancer Well, we can't tell if it's cancer or not right now But what we'll do is we'll run all these tests and then we'll make it and then we'll have some more information after that And I'll see you again in four weeks time to discuss the plan going forward does that make sense? Yes, doctor Do you have any questions for me at the moment? No, thank you very much."""

ASSISTANT_output = """[Your Name]
[Your Title and Specialty]
[Your Clinic or Hospital]
[Date]

Patient: Adam
Date of Consultation: [Date]

Dear Adam,

I hope this letter finds you well. I am writing to summarize our recent conversation regarding the symptoms you've been experiencing and the proposed course of action to determine the underlying cause.

During our discussion, you mentioned that you have been experiencing pain in your abdomen along with unintentional weight loss over the past three and a half months. You also reported bloating and loose stool, with a frequency of twice a day. Additionally, you mentioned that you have not been intentionally dieting. I appreciate you sharing this information, and I understand your concern regarding these symptoms.

In light of your symptoms and the possibility of an underlying medical condition, we have discussed a comprehensive approach to identify the cause. Given the complexity of your situation, I have recommended the following investigations:

CT Scan of the Abdomen and Pelvis: This will help us assess the condition of your abdominal organs and identify any potential abnormalities.

CT Scan of the Chest: To ensure a thorough evaluation, we will also conduct a scan of your chest.

Stool Analysis: A sample of your stool will be collected for analysis, which can provide us with valuable insights into your gastrointestinal health.

Blood Tests: A series of blood tests will be conducted, including a full blood count, liver function tests, urea and renal function tests, calcium levels, and other relevant markers such as tumor markers.

While it is natural to have concerns about your health, it's important to note that we cannot definitively diagnose any condition at this point. The investigations outlined above will allow us to gather more information and make an informed decision regarding the next steps in your care.

You expressed apprehension about the possibility of cancer. While we cannot rule out any possibilities just yet, it's crucial to remember that our goal is to comprehensively assess your health and provide you with accurate information about your condition.

Following the completion of the above tests, I would like to schedule a follow-up appointment with you in approximately four weeks. During this appointment, we will discuss the results of the investigations and formulate a suitable plan based on the information available.

Please feel free to reach out if you have any questions or concerns in the meantime. Your well-being is our priority, and I am here to support you throughout this process.

Thank you for entrusting me with your care. We will work together to understand your health better and make informed decisions regarding your treatment.

Sincerely,

[Your Name]
[Your Title and Specialty]
[Contact Information]"""