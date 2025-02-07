import FWCore.ParameterSet.Config as cms

def ModifiedGsfElectronProducer(*args, **kwargs):
  mod = cms.EDProducer('ModifiedGsfElectronProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
