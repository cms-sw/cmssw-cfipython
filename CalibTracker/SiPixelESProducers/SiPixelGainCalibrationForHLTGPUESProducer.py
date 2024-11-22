import FWCore.ParameterSet.Config as cms

def SiPixelGainCalibrationForHLTGPUESProducer(*args, **kwargs):
  mod = cms.ESProducer('SiPixelGainCalibrationForHLTGPUESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
