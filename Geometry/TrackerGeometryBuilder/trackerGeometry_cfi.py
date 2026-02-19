import FWCore.ParameterSet.Config as cms

from .TrackerDigiGeometryESModule import TrackerDigiGeometryESModule

trackerGeometry = TrackerDigiGeometryESModule(

  fromDDD = True
)
