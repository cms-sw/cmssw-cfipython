import FWCore.ParameterSet.Config as cms

def EcalPhiSymRecHitFlatTableProducerRun(**kwargs):
  mod = cms.EDProducer('EcalPhiSymRecHitFlatTableProducerRun',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
