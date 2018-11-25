from video_player import VideoPlayer

import json

PEOPLE_FLOW_POINTS_JSON_PATH = '../data/people_flow_points.json'

VIDEO_PATHS = [
    ('../data/videos_detected/VID_20181124_220745.mp4',
     '../data/videos_detected/VID_20181124_221745.mp4',
     '../data/videos_detected/VID_20181124_223626.mp4'),
    ('../data/videos_detected/VID_20181124_220828.mp4',
     '../data/videos_detected/VID_20181124_221830.mp4',
     '../data/videos_detected/VID_20181124_223718.mp4'),
    ('../data/videos_detected/VID_20181124_220902.mp4',
     '../data/videos_detected/VID_20181124_222009.mp4',
     '../data/videos_detected/VID_20181124_223805.mp4'),
    ('../data/videos_detected/VID_20181124_221133.mp4',
     '../data/videos_detected/VID_20181124_221133.mp4',
     '../data/videos_detected/VID_20181124_223906.mp4'),
    ('../data/videos_detected/VID_20181124_222620.mp4',
     '../data/videos_detected/VID_20181124_222620.mp4',
     '../data/videos_detected/VID_20181124_222620.mp4'),
    ('../data/videos_detected/VID_20181124_222818.mp4',
     '../data/videos_detected/VID_20181124_222818.mp4',
     '../data/videos_detected/VID_20181124_222818.mp4'),
    ('../data/videos_detected/VID_20181124_222957.mp4',
     '../data/videos_detected/VID_20181124_222957.mp4',
     '../data/videos_detected/VID_20181124_222957.mp4'),
    ('../data/videos_detected/VID_20181124_223100.mp4',
     '../data/videos_detected/VID_20181124_223100.mp4',
     '../data/videos_detected/VID_20181124_223100.mp4')
]


class System:
    def __init__(self):
        self._video_group = []
        self._cur_vgroup = 0
        self._subscribers_on_videos = []
        self.init_video_group()
        self._point_groups = self.load_points(PEOPLE_FLOW_POINTS_JSON_PATH)

    def init_video_group(self):
        if len(VIDEO_PATHS) == 0:
            return

        self._cur_vgroup = 0

        group_paths = VIDEO_PATHS[self._cur_vgroup]
        for gr_path in group_paths:
            video_player = VideoPlayer(gr_path)
            self._video_group.append(video_player)

    def next_video(self):
        self.stop_video_group()

        group_paths = VIDEO_PATHS[self._cur_vgroup]
        for gr_path in group_paths:
            video_player = VideoPlayer(gr_path)
            self._video_group.append(video_player)
        for subscr_funcs in self._subscribers_on_videos:
            self._apply_subscription_on_videos(*subscr_funcs)

        self._cur_vgroup = (self._cur_vgroup + 1) % len(VIDEO_PATHS)
        self.play_video_group()

    def play_video_group(self):
        for video_player in self._video_group:
            video_player.play()

    def pause_video_group(self):
        for video_player in self._video_group:
            video_player.pause()

    def stop_video_group(self):
        for video_player in self._video_group:
            video_player.stop()

        self._video_group = []

    def subscribe_on_videos(self, subscr_func1, subscr_func2, subscr_func3):
        self._apply_subscription_on_videos(subscr_func1, subscr_func2, subscr_func3)
        self._subscribers_on_videos.append((subscr_func1, subscr_func2, subscr_func3))

    def _apply_subscription_on_videos(self, subscr_func1, subscr_func2, subscr_func3):
        if len(self._video_group) < 3:
            return

        self._video_group[0].add_subscriber(subscr_func1)
        self._video_group[1].add_subscriber(subscr_func2)
        self._video_group[2].add_subscriber(subscr_func3)

    def load_points(self, json_path):
        with open(json_path, 'r') as f:
            pflow_points = json.load(f)

        point_groups = []
        colors = [(0, 255, 0, 255), (0, 0, 255, 255), (255, 0, 0, 255)]
        i = 0
        for person_name, geoms in pflow_points[0]['Label'].items():
            points = []
            for geom in geoms:
                point = {'x': geom['geometry']['x'],
                         'y': geom['geometry']['y'],
                         'color': colors[i]}
                points.append(point)
            point_groups.append(points)
            i += 1

        return point_groups
