import FWCore.ParameterSet.Config as cms

def PPSTimingCalibrationLUTESSource(*args, **kwargs):
  mod = cms.ESSource('PPSTimingCalibrationLUTESSource',
    calibrationFile = cms.FileInPath(''),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
