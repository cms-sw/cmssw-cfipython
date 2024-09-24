import FWCore.ParameterSet.Config as cms

def trgMatchGsfElectronProducer(*args, **kwargs):
  mod = cms.EDProducer('trgMatchGsfElectronProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod