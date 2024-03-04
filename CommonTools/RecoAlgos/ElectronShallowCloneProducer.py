import FWCore.ParameterSet.Config as cms

def ElectronShallowCloneProducer(**kwargs):
  mod = cms.EDProducer('ElectronShallowCloneProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
