import FWCore.ParameterSet.Config as cms

def SiPixelCalibDigiFilter(**kwargs):
  mod = cms.EDFilter('SiPixelCalibDigiFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
