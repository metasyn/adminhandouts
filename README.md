# Admin Handouts 

These two templates along with the accompaning script can be used to generate handouts for the Splunk Administration class. 

If you're interested in using them, I've outlined the steps before.

# Download the files

The two easiest options are:

1. cloning the repository with `git clone http://github.com/metasyn/adminhandouts.git`
2. clicking the clone or download button to download a zip of the repository

![](http://i.imgur.com/wnBWlPP.png)

# Running the script 

It's really pretty trivial. It should run with python 2 or 3. Simply:

`python server_assinger.py students.csv`

where `students.csv` is the output from the dispatcher script. Copy-paste or scp the list file created to the folder in which you run the script. It will then make a folder called `server_assignments` and put the handouts there.

You can see an example of what it would look like [here](https://rawgit.com/metasyn/adminhandouts/master/template_linux.html).

# Disabling animation

Simply comment out or remove this portion of the template:

```

      @keyframes dash {
        to {
          stroke-dashoffset: 1000;
        }
      }
```

and there should be no more movement.

# Browser and OS support

I've tested it on OSX El Capitan on:

 - Safari 9.1.1
 - Firefox 48
 - Chrome 52.0.2743.116

On Windows, I tested on Windows Server and found that the animations did not work but the toggles and connections all showed up fine on IE and Firefox. 
