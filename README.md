# Tech_quizz
A little interface program to play quizz with the quizapi.
It wraps the API's use and count the score.

## First Step

You need to claim an API KEY here https://quizapi.io/clientarea and enter it the config file config.json like this :

```json
{
  "api_key": "Your_Api_Key_Here"
}
```

You can find all the documentation about the API right here : https://quizapi.io/docs/1.0/overview.

## Using the code

You can see a code's example in the main.py file. 

```python
Quizz_test_init = API_Call_to_send(difficulty="easy", category="Docker", number_of_question=2)
```

All you have to do is to enter the difficulty, the category and the number of questions you want and after that, all your commands/answers will be in the console.
