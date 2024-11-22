import FWCore.ParameterSet.Config as cms

def ESGainPopConTransitionAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ESGainPopConTransitionAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
