from PyQt5 import QtCore, QtWidgets

from custom_widgets import MapField
from gui_utils import cvt_numpy_to_qscene

import cv2
import random
import json

PEOPLE_FLOW_POINTS_JSON_PATH = '../data/people_flow_points.json'


class SlotsHandler:
    def __init__(self, ui, tab_widget, system):
        self._ui = ui
        self._tab_widget = tab_widget
        self._system = system
        self.init_ui()
        self._point_groups = self.load_points(PEOPLE_FLOW_POINTS_JSON_PATH)
        self._cur_point_group = 0

    def init_ui(self):
        self._ui.startBtn.clicked.connect(self.start_videos)
        self._ui.pauseBtn.clicked.connect(self.pause_videos)
        self._ui.stopBtn.clicked.connect(self.stop_videos)

        img = cv2.imread('./assets/junction_floor1.png')[..., ::-1]
        h, w = img.shape[:2]
        new_h, new_w = 512, int(512 * w / h)
        self._map_shape = new_h, new_w
        img = cv2.resize(img, (new_w, new_h))
        scene = cvt_numpy_to_qscene(img)
        self._ui.graphicsView.setScene(scene)

        self.map_field = MapField(img.shape)
        self._ui.mapLayout.addWidget(self.map_field)

        # self._ui.startBtn.clicked.connect(self.add_point_on_map)

        self._system.subscribe_on_videos(self.update_video_frame1, self.update_video_frame2,
                                         self.update_video_frame3)

    def start_videos(self):
        self._system.play_video_group()

        if self._cur_point_group == 0:
            self.clear_points()
        self._cur_point_group = self._cur_point_group = (self._cur_point_group + 1) % \
                                                        len(self._point_groups[0])
        self.add_point_on_map()

    def pause_videos(self):
        self._system.pause_video_group()

    def stop_videos(self):
        self._system.stop_video_group()

    def add_point_on_map(self):
        for point_slice in self._point_groups:
            point = point_slice[self._cur_point_group]

            x = int(point['x'] / 3308 * self._map_shape[1])
            y = int(point['y'] / 2338 * self._map_shape[0])
            color = point['color']

            self.map_field.add_point(x, y, color)

    def clear_points(self):
        self.map_field.clear_points()

    def update_video_frame1(self, is_playing, img):
        scene = cvt_numpy_to_qscene(img)
        self._ui.cameraView1.setScene(scene)

        if not is_playing:
            self._system.next_video()
            self._cur_point_group = (self._cur_point_group + 1) % \
                                    len(self._point_groups[0])
            if self._cur_point_group == 0:
                self.clear_points()
            self.add_point_on_map()

    def update_video_frame2(self, is_playing, img):
        scene = cvt_numpy_to_qscene(img)
        self._ui.cameraView2.setScene(scene)

    def update_video_frame3(self, is_playing, img):
        scene = cvt_numpy_to_qscene(img)
        self._ui.cameraView3.setScene(scene)

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
