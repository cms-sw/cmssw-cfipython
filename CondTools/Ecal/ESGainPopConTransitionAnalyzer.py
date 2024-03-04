import FWCore.ParameterSet.Config as cms

def ESGainPopConTransitionAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ESGainPopConTransitionAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
