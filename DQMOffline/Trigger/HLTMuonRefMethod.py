import FWCore.ParameterSet.Config as cms

def HLTMuonRefMethod(**kwargs):
  mod = cms.EDProducer('HLTMuonRefMethod',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
