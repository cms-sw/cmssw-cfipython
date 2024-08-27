import FWCore.ParameterSet.Config as cms

def L1TPhase2MuonOffline(**kwargs):
  mod = cms.EDProducer('L1TPhase2MuonOffline',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
