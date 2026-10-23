import FWCore.ParameterSet.Config as cms

def ESTimeSampleWeightsPopConTransitionAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ESTimeSampleWeightsPopConTransitionAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
