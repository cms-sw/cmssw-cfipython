import FWCore.ParameterSet.Config as cms

def L1TMuonDQMOffline(**kwargs):
  mod = cms.EDProducer('L1TMuonDQMOffline',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
