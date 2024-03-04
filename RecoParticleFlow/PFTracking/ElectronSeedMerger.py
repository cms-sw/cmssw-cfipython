import FWCore.ParameterSet.Config as cms

def ElectronSeedMerger(**kwargs):
  mod = cms.EDProducer('ElectronSeedMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
