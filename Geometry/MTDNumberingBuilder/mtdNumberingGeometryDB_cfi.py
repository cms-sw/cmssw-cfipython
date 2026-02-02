import FWCore.ParameterSet.Config as cms

from .MTDGeometricTimingDetESModule import MTDGeometricTimingDetESModule

mtdNumberingGeometryDB = MTDGeometricTimingDetESModule(
  fromDDD = False,
  fromDD4hep = False,
  appendToDataLabel = ''
)
