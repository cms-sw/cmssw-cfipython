import FWCore.ParameterSet.Config as cms

def ESTimeSampleWeightsPopConTransitionAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ESTimeSampleWeightsPopConTransitionAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
