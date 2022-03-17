import discord
import openai
from os import system
from keep_alive import keep_alive

keep_alive()

openai.api_key = "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"


def translate_text(text):
    response = openai.Completion.create(engine="text-davinci-002",
                                        prompt=text,
                                        temperature=0,
                                        max_tokens=1500,
                                        top_p=1.0,
                                        frequency_penalty=0.0,
                                        presence_penalty=0.0,
                                        stop=["###"])

    return response.choices[0].text

def autocomplete_text(code):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=code,
        temperature=0,
        max_tokens=1500,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["###"]
    )

    return response.choices[0].text

def explain_code(code):
    response = openai.Completion.create(engine="text-davinci-002",
                                        prompt=code,
                                        temperature=0,
                                        max_tokens=64,
                                        top_p=1.0,
                                        frequency_penalty=0.0,
                                        presence_penalty=0.5,
                                        stop=["\"\"\""])

    return response.choices[0].text


class main(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

        if (message.content.find('/code') != -1):
            code_explain = explain_code(
                message.content.split("/code", 1)[1] +
                "What this code make?\"\"\"")
            print(code_explain)
            await message.channel.send(
                f'{message.author} A resposta do seu codigo : \n\n{code_explain}'
            )
        if (message.content.find('/translate') != -1):
            message_natural = message.content.split('/translate', 1)[1]
            translate_code = translate_text(
                f"##### Translate this text from Natural language into Python\n### Natural language\n{message_natural}\n### Python"
            )
            print(translate_code)
            await message.channel.send(
                f'{message.author} Consegui traduzir oque você falou está aqui : \n\n{translate_code}'
            )

        if (message.content.find('/autocomplete') != -1):
            message_to_complete = message.content.split('/autocomplete', 1)[1]
            autocomplete_code = autocomplete_text(
                f"#####Sugest autocompletes for my code###{message_to_complete}\n###"
            )
            print(autocomplete_code)
            await message.channel.send(
                f'{message.author} Consegui completar oque você falou está aqui : \n\n{autocomplete_code.rstrip('\n')}'
            )


client = main()

try:
    client.run('OTUzNjM0NTE3NzQ5NDkzODMx.YjHbWg.RFauWQyuo6rAVS5DDiC8Q93vTJg')
except discord.errors.HTTPException:
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
