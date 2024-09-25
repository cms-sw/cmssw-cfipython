import FWCore.ParameterSet.Config as cms

def DeleteEarlyCheckDeleteAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('DeleteEarlyCheckDeleteAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
