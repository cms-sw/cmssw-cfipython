import FWCore.ParameterSet.Config as cms

def EcalPhiSymRecHitProducerLumi(**kwargs):
  mod = cms.EDProducer('EcalPhiSymRecHitProducerLumi',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
