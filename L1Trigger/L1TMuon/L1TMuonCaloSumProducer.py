import FWCore.ParameterSet.Config as cms

def L1TMuonCaloSumProducer(**kwargs):
  mod = cms.EDProducer('L1TMuonCaloSumProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
