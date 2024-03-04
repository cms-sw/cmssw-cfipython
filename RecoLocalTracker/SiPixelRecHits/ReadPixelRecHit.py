import FWCore.ParameterSet.Config as cms

def ReadPixelRecHit(**kwargs):
  mod = cms.EDAnalyzer('ReadPixelRecHit',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
