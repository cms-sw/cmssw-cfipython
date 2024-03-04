import FWCore.ParameterSet.Config as cms

def MuonGEMDigisHarvestor(**kwargs):
  mod = cms.EDProducer('MuonGEMDigisHarvestor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
