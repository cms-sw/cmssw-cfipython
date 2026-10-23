import FWCore.ParameterSet.Config as cms

def EcalPhiSymRecHitProducerRun(*args, **kwargs):
  mod = cms.EDProducer('EcalPhiSymRecHitProducerRun',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
