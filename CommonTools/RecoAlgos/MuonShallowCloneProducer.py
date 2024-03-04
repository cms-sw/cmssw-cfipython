import FWCore.ParameterSet.Config as cms

def MuonShallowCloneProducer(**kwargs):
  mod = cms.EDProducer('MuonShallowCloneProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
