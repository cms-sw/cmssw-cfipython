import FWCore.ParameterSet.Config as cms

def EcalRecHitColCleaner(**kwargs):
  mod = cms.EDProducer('EcalRecHitColCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
