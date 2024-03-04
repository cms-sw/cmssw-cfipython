import FWCore.ParameterSet.Config as cms

def MuonGEMHitsHarvestor(**kwargs):
  mod = cms.EDProducer('MuonGEMHitsHarvestor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
