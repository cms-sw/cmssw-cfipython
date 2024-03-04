import FWCore.ParameterSet.Config as cms

def SiPixelGainCalibrationForHLTGPUESProducer(**kwargs):
  mod = cms.ESProducer('SiPixelGainCalibrationForHLTGPUESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
