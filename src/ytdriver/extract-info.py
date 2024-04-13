from ytdriver import YTDriver
# import importlib  # Import your module if not already imported
# importlib.reload(ytdriver)  
import json

def save_json(data, filename):
    """
    Saves the given data to a JSON file.
    
    Args:
        data (dict): A Python dictionary containing data to be saved as JSON.
        filename (str): The name of the file to which the JSON data will be written.
    """
    try:
        # Writing JSON data
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Data successfully saved to {filename}")
    except Exception as e:
        print(f"An error occurred while writing JSON to the file: {e}")



if __name__ == '__main__':
  # initialize the driver
  driver = YTDriver(browser='firefox', verbose=True)

  # get videos from the youtube homepage
  videos = driver.get_homepage()
  video = driver.watch_video_by_link('https://www.youtube.com/watch?v=nTdR-j-KjNk')
  metadata = video.get_metadata()
  print(metadata['title'])
  # videos = driver.search_videos('sports')

  # # play the top video from the homepage for 30 seconds
  # driver.play(videos[0], 30)

  # # get up-next video recommendations
  # for video in driver.get_recommendations():
  #   metadata = video.get_metadata()
  #   print(metadata['title'])
  #   print('-----------------------------------------------------------')
  #   print(metadata)
  #   save_json(metadata, './data/metadata.json')
  #   break

  # print('-----------------------------------------------------------')

  # # search for a keyword
  # for video in driver.search_videos('sports'):
  #   print(video.url)
    
  # close driver
  driver.close()