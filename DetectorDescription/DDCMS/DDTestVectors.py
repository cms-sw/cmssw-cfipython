import FWCore.ParameterSet.Config as cms

def DDTestVectors(*args, **kwargs):
  mod = cms.EDAnalyzer('DDTestVectors',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
