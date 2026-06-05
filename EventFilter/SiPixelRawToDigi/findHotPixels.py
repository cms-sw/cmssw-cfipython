import FWCore.ParameterSet.Config as cms

def findHotPixels(*args, **kwargs):
  mod = cms.EDAnalyzer('findHotPixels',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
