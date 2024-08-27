import FWCore.ParameterSet.Config as cms

def MuonSeedMerger(**kwargs):
  mod = cms.EDProducer('MuonSeedMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
