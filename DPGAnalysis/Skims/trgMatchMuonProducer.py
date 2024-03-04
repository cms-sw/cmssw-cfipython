import FWCore.ParameterSet.Config as cms

def trgMatchMuonProducer(**kwargs):
  mod = cms.EDProducer('trgMatchMuonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
