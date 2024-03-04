import FWCore.ParameterSet.Config as cms

def trgMatchedMuonProducer(**kwargs):
  mod = cms.EDProducer('trgMatchedMuonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
