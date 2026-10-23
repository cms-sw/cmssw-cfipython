import FWCore.ParameterSet.Config as cms

def TauValElectronViewCleaner(*args, **kwargs):
  mod = cms.EDProducer('TauValElectronViewCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
