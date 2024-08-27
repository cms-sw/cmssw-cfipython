import FWCore.ParameterSet.Config as cms

def HcalRecHitsAnalyzer(**kwargs):
  mod = cms.EDProducer('HcalRecHitsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
