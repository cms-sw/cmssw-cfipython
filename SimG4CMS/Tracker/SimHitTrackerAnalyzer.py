import FWCore.ParameterSet.Config as cms

def SimHitTrackerAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('SimHitTrackerAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod