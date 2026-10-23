import FWCore.ParameterSet.Config as cms

def PathAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('PathAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
