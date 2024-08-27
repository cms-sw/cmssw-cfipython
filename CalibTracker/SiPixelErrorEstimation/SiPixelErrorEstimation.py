import FWCore.ParameterSet.Config as cms

def SiPixelErrorEstimation(**kwargs):
  mod = cms.EDAnalyzer('SiPixelErrorEstimation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
