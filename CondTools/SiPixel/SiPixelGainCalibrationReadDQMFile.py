import FWCore.ParameterSet.Config as cms

def SiPixelGainCalibrationReadDQMFile(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelGainCalibrationReadDQMFile',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
