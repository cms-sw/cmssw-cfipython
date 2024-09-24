import FWCore.ParameterSet.Config as cms

def ModifiedElectronProducer(*args, **kwargs):
  mod = cms.EDProducer('ModifiedElectronProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod