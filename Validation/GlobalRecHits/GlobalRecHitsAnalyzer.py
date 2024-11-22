import FWCore.ParameterSet.Config as cms

def GlobalRecHitsAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('GlobalRecHitsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
