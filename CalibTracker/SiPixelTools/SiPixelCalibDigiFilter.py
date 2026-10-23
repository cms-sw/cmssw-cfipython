import FWCore.ParameterSet.Config as cms

def SiPixelCalibDigiFilter(*args, **kwargs):
  mod = cms.EDFilter('SiPixelCalibDigiFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
