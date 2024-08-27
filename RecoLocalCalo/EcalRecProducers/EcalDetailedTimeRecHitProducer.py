import FWCore.ParameterSet.Config as cms

def EcalDetailedTimeRecHitProducer(**kwargs):
  mod = cms.EDProducer('EcalDetailedTimeRecHitProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
