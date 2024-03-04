import FWCore.ParameterSet.Config as cms

def EcalTBWeightUncalibRecHitProducer(**kwargs):
  mod = cms.EDProducer('EcalTBWeightUncalibRecHitProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
