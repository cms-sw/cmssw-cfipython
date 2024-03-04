import FWCore.ParameterSet.Config as cms

def ElectronOfflineClient(**kwargs):
  mod = cms.EDProducer('ElectronOfflineClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
