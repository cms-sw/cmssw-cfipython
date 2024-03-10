import FWCore.ParameterSet.Config as cms

def PPSTimingCalibrationESSource(**kwargs):
  mod = cms.ESSource('PPSTimingCalibrationESSource',
    calibrationFile = cms.FileInPath(),
    subDetector = cms.uint32(0),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
