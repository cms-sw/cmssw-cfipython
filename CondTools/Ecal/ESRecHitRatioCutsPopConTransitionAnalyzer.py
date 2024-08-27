import FWCore.ParameterSet.Config as cms

def ESRecHitRatioCutsPopConTransitionAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ESRecHitRatioCutsPopConTransitionAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
