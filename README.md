# AgendIA
Assistant Automatique d'Agenda

## Requirement
To compile this project, you need the Framework ASP.NET Core 3.1.

## Installation
Simply clone this project by running following command:
```bash
git clone https://github.com/Picrik/AgendIA.git
```

To compile this project, run with the required Framework active following command:
```bash
dotnet build
dotnet run
```

## Usage
After compiling this project, run the created .exe file available in bin folder.
This will give you access to a localhostWebApp.

### jsonBase
In this project, a folder contains every json associated to every service account.
Those json are named under the pseudonym of the user account.

### ApiGet
You can send to a json a new event to treat by associating with pseudonym.
GET command is as follows:
```bash
localhost:[port]/events/AddEvent?PersonId=[pseudo]&Maker=[Name]&StartDateTime=[dd-mm-yyyy-hh-mm]&EndDateTime=[dd-mm-yyyy-hh-mm]&Subject=[subject]
```

### Integration with IBM Chatbot
After logging to an account, you can see a little chatbotaccess in bottom right corner. The POST method is not yet implemented,but you can talk with the chatbot.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Share and social media
If you have any question, feel free to reach me on https://twitter.com/lilixns.

