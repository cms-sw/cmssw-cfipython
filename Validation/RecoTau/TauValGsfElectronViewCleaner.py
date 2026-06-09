import FWCore.ParameterSet.Config as cms

def TauValGsfElectronViewCleaner(*args, **kwargs):
  mod = cms.EDProducer('TauValGsfElectronViewCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
