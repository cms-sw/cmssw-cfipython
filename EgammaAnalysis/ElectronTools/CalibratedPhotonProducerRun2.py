import FWCore.ParameterSet.Config as cms

def CalibratedPhotonProducerRun2(**kwargs):
  mod = cms.EDProducer('CalibratedPhotonProducerRun2',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
