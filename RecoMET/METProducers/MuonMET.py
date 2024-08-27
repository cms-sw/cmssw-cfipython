import FWCore.ParameterSet.Config as cms

def MuonMET(**kwargs):
  mod = cms.EDProducer('MuonMET',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
