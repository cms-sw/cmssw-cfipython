import FWCore.ParameterSet.Config as cms

def RecoMuonValidator(**kwargs):
  mod = cms.EDProducer('RecoMuonValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
