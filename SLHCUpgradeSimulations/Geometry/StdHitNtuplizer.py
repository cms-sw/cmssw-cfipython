import FWCore.ParameterSet.Config as cms

def StdHitNtuplizer(*args, **kwargs):
  mod = cms.EDAnalyzer('StdHitNtuplizer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
