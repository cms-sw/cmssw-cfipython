import FWCore.ParameterSet.Config as cms

def CalibratedPatElectronProducerRun2(**kwargs):
  mod = cms.EDProducer('CalibratedPatElectronProducerRun2',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
