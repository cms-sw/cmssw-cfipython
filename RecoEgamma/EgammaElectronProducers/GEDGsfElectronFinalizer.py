import FWCore.ParameterSet.Config as cms

def GEDGsfElectronFinalizer(*args, **kwargs):
  mod = cms.EDProducer('GEDGsfElectronFinalizer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
