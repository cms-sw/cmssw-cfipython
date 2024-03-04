import FWCore.ParameterSet.Config as cms

def L3TkMuonProducer(**kwargs):
  mod = cms.EDProducer('L3TkMuonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
