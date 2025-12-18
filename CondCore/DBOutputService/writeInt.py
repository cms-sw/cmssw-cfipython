import FWCore.ParameterSet.Config as cms

def writeInt(*args, **kwargs):
  mod = cms.EDAnalyzer('writeInt',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
