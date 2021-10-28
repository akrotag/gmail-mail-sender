# Gmail email sender

Gmail email sender (yeah I was really inspired for the name) is a simple python terminal script that allows you to send emails to anyone as long as you have a gmail account

## Installation

Simply download the code or use the git clone command to clone the repository

```bash
git clone https://github.com/akrotag/gmail-mail-sender.git
```

## Usage

```bash
gmail_sender.py -ue "your email" -p "your password" -r "the receiver's email" -s "subject of the mail" -t "the body/content of the mail" -a "attachment's path(if you have any attachment to put)"
```
Details:
-

-You can use a "\n" to break the body

-There is only three(3) mandatory commands that are: -ue, -p and -r

## Limitations
There is only one important limitations: Your attachment can't weight more than 25MB due to [gmail's attachemnt size limit](https://support.google.com/mail/?p=MaxSizeError)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

I would just ask you to please comment your code, not necessarily as much as I did but at least for it to be understandable by a beginner

Please make sure to update tests as appropriate.
