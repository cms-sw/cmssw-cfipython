import FWCore.ParameterSet.Config as cms

def CalibratedPatPhotonProducerRun2(*args, **kwargs):
  mod = cms.EDProducer('CalibratedPatPhotonProducerRun2',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
