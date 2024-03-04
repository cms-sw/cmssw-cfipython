import FWCore.ParameterSet.Config as cms

def L1TMuonProducer(**kwargs):
  mod = cms.EDProducer('L1TMuonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
