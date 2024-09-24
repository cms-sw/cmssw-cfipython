import FWCore.ParameterSet.Config as cms

def DuplicatedElectronCleaner(*args, **kwargs):
  mod = cms.EDProducer('DuplicatedElectronCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
