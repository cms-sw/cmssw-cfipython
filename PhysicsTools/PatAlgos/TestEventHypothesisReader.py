import FWCore.ParameterSet.Config as cms

def TestEventHypothesisReader(*args, **kwargs):
  mod = cms.EDAnalyzer('TestEventHypothesisReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
