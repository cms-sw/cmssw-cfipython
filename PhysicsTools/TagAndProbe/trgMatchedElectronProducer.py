import FWCore.ParameterSet.Config as cms

def trgMatchedElectronProducer(*args, **kwargs):
  mod = cms.EDProducer('trgMatchedElectronProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
