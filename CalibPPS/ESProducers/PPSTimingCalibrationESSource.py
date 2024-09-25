import FWCore.ParameterSet.Config as cms

def PPSTimingCalibrationESSource(*args, **kwargs):
  mod = cms.ESSource('PPSTimingCalibrationESSource',
    calibrationFile = cms.FileInPath(''),
    subDetector = cms.uint32(0),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
