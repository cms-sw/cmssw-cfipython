import FWCore.ParameterSet.Config as cms

def MuonColMerger(**kwargs):
  mod = cms.EDProducer('MuonColMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
