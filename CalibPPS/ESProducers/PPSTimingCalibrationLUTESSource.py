import FWCore.ParameterSet.Config as cms

def PPSTimingCalibrationLUTESSource(**kwargs):
  mod = cms.ESSource('PPSTimingCalibrationLUTESSource',
    calibrationFile = cms.FileInPath(''),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
