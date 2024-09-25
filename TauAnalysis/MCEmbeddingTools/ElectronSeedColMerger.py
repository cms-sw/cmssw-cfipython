import FWCore.ParameterSet.Config as cms

def ElectronSeedColMerger(*args, **kwargs):
  mod = cms.EDProducer('ElectronSeedColMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
