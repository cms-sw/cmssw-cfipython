import FWCore.ParameterSet.Config as cms

def MuonProducer(**kwargs):
  mod = cms.EDProducer('MuonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
