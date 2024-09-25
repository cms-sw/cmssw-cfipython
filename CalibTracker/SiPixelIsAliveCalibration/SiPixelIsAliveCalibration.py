import FWCore.ParameterSet.Config as cms

def SiPixelIsAliveCalibration(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelIsAliveCalibration',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
