import FWCore.ParameterSet.Config as cms

def TevMuonProducer(**kwargs):
  mod = cms.EDProducer('TevMuonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
