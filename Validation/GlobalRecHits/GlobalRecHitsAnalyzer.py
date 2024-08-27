import FWCore.ParameterSet.Config as cms

def GlobalRecHitsAnalyzer(**kwargs):
  mod = cms.EDProducer('GlobalRecHitsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
