import FWCore.ParameterSet.Config as cms

def PATElectronCleaner(*args, **kwargs):
  mod = cms.EDProducer('PATElectronCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
