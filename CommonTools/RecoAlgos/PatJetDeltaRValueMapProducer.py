import FWCore.ParameterSet.Config as cms

def PatJetDeltaRValueMapProducer(**kwargs):
  mod = cms.EDProducer('PatJetDeltaRValueMapProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
