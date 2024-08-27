import FWCore.ParameterSet.Config as cms

def ElectronSeedColMerger(**kwargs):
  mod = cms.EDProducer('ElectronSeedColMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
