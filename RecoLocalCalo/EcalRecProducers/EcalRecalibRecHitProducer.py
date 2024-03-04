import FWCore.ParameterSet.Config as cms

def EcalRecalibRecHitProducer(**kwargs):
  mod = cms.EDProducer('EcalRecalibRecHitProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
