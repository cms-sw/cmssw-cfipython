import FWCore.ParameterSet.Config as cms

def HLTTauMCProducer(**kwargs):
  mod = cms.EDProducer('HLTTauMCProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
