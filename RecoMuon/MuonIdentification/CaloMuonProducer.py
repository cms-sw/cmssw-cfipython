import FWCore.ParameterSet.Config as cms

def CaloMuonProducer(**kwargs):
  mod = cms.EDProducer('CaloMuonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
