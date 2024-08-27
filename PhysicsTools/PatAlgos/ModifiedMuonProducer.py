import FWCore.ParameterSet.Config as cms

def ModifiedMuonProducer(**kwargs):
  mod = cms.EDProducer('ModifiedMuonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
