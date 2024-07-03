import FWCore.ParameterSet.Config as cms

def HcalRecHitSoAToLegacy(**kwargs):
  mod = cms.EDProducer('HcalRecHitSoAToLegacy',
    src = cms.InputTag('hbheRecHitProducerPortable'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
