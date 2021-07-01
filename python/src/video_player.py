"""A video player class."""
import random

from .video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.vid_playing = False
        self.vid_paused = True
        self.vid_name = None

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")


    def show_all_videos(self):
        """Returns all videos."""
        # The get_all_videos command comes from video_library
        videos = self._video_library.get_all_videos()
        print("Here's a list of all available videos:")
        temp_list = []
        # Creates the temp_list object

        for vid in videos:
            # Convoluted way to display tags in required format
            tags = "["
            for tag in vid.tags:
                tags = tags + tag + " "
            tags = tags + "]"

            if tags != "[]":
                tags = tags[0:len(tags) - 2] + "]"

            # Put all videos in a list for sorting
            temp_list += [f"{vid.title} ({vid.video_id}) {tags}"]

        # Sort the list in alphabetical order and display
        sorted_list = sorted(temp_list)
        for x in sorted_list:
            print(x)


    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        now_playing = self._video_library.get_video(video_id)

        # Try function - follows code until it encounters an error (ie. nonexistent video)
        try:
            if self.vid_playing is True:
                if not now_playing:
                    print("Cannot play video: Video does not exist")
                else:
                    print(f"Stopping video: {self.vid_name}")
                    print(f"Playing video: {now_playing.title}")
                    self.vid_name = now_playing.title
                    self.vid_paused = False
            else:
                print(f"Playing video: {now_playing.title}")
                self.vid_playing = True
                self.vid_paused = False
                self.vid_name = now_playing.title
        except:
            print("Cannot play video: Video does not exist")


    def stop_video(self):
        """Stops the current video."""
        if self.vid_playing is True:
            print(f"Stopping video: {self.vid_name}")
            self.vid_playing = False
            self.vid_paused = True
            self.vid_name = None
        else:
            if self.vid_playing is False:
                print("Cannot stop video: No video is currently playing")
                self.vid_paused = True


    def play_random_video(self):
        """Plays a random video from the video library."""
        ran_vid = random.choice(self._video_library.get_all_videos())

        if self.vid_playing is True:
            print(f"Stopping video: {self.vid_name}")
        print(f"Playing video: {ran_vid.title}")
        self.vid_paused = False
        self.vid_name = ran_vid.title


    def pause_video(self):
        """Pauses the current video."""
        if self.vid_playing is False:
            print("Cannot pause video: No video is currently playing")
            self.vid_name = None
        else:
            if self.vid_paused is True:
                print(f"Video already paused: {self.vid_name}")
                self.vid_playing = False
            else:
                print(f"Pausing video: {self.vid_name}")
                self.vid_paused = True
                self.vid_name = self.vid_name


    def continue_video(self):
        """Resumes playing the current video."""
        if self.vid_name is None:
            print("Cannot continue video: No video is currently playing")
        else:
            if self.vid_paused is True:
                print(f"Continuing video: {self.vid_name}")
                self.vid_playing = True
                self.vid_paused = False
            else:
                print("Cannot continue video: Video is not paused")


    def show_playing(self):
        """Displays video currently playing."""

        if self.vid_name is None:
            print("No video is currently playing")
        else:
            if self.vid_paused is True:
                print(f"Currently playing: {self.vid_name} (??)" "\n"
                      "[??] - PAUSED")
            else:
                print(f"Currently playing: {self.vid_name} (??) [??]")

# I ran out of time to figure out how to extract the other video information.

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
