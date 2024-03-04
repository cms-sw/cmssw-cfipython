import FWCore.ParameterSet.Config as cms

def TrackerHitAnalyzer(**kwargs):
  mod = cms.EDProducer('TrackerHitAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
