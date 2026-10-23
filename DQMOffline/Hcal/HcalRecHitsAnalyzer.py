import FWCore.ParameterSet.Config as cms

def HcalRecHitsAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('HcalRecHitsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
