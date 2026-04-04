import FWCore.ParameterSet.Config as cms

def trgMatchElectronProducer(*args, **kwargs):
  mod = cms.EDProducer('trgMatchElectronProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
