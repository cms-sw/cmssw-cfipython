import FWCore.ParameterSet.Config as cms

def SiPixelGainCalibrationReadDQMFile(**kwargs):
  mod = cms.EDAnalyzer('SiPixelGainCalibrationReadDQMFile',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
