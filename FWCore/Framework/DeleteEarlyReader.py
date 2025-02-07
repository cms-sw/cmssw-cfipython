import FWCore.ParameterSet.Config as cms

def DeleteEarlyReader(*args, **kwargs):
  mod = cms.EDAnalyzer('DeleteEarlyReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
