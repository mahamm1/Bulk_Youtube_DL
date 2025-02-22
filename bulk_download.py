from pytube import YouTube

save_path = 'Directory for saving the files'

# Reading links from text files
link = open('links.txt', 'r')

# For links count
count = 0

for i in (link):
    try:
        # Fetxhing youtube details of provided link
        x = YouTube(i)

        print('Starting to download ' + x.title)
        # Applying progressive download
        x.streams.filter(progressive="true")

        # Downloading first quality video
        x.streams.get_highest_resolution().download(save_path)

        print('Finished downloading ' + x.title)

        print('-------------------------------------' + "\n")
        # Increasing count of the link as it completes the downloading
        count = count + 1

    except:
        print("Error")

print('All Links fetched from text file')
print('Total link downloaded ' + str(count))

