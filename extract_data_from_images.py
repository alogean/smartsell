# Images to extract data from
fruits = ['https://storage.googleapis.com/vectrix-public/fruit/apple.jpeg',
          'https://storage.googleapis.com/vectrix-public/fruit/banana.jpeg',
          'https://storage.googleapis.com/vectrix-public/fruit/kiwi.jpeg',
          'https://storage.googleapis.com/vectrix-public/fruit/peach.jpeg',
          'https://storage.googleapis.com/vectrix-public/fruit/plum.jpeg']

image_path = "./photo_slips.jpg"
user_question = "generate a caption for this iamge?"
response = agent.run(f'{user_question}, this is the image path: {image_path}')
print(response)
