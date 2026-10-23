import FWCore.ParameterSet.Config as cms

def ElectronIdMVAProducer(*args, **kwargs):
  mod = cms.EDFilter('ElectronIdMVAProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
