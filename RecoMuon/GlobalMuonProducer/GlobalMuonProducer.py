import FWCore.ParameterSet.Config as cms

def GlobalMuonProducer(**kwargs):
  mod = cms.EDProducer('GlobalMuonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
