import FWCore.ParameterSet.Config as cms

def ReadPixelRecHit(*args, **kwargs):
  mod = cms.EDAnalyzer('ReadPixelRecHit',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
