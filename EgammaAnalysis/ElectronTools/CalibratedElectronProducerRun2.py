import FWCore.ParameterSet.Config as cms

def CalibratedElectronProducerRun2(**kwargs):
  mod = cms.EDProducer('CalibratedElectronProducerRun2',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
