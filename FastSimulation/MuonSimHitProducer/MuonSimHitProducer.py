import FWCore.ParameterSet.Config as cms

def MuonSimHitProducer(**kwargs):
  mod = cms.EDProducer('MuonSimHitProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
