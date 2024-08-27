import FWCore.ParameterSet.Config as cms

def MuonRefProducer(**kwargs):
  mod = cms.EDProducer('MuonRefProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
