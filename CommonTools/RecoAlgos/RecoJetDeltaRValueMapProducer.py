import FWCore.ParameterSet.Config as cms

def RecoJetDeltaRValueMapProducer(**kwargs):
  mod = cms.EDProducer('RecoJetDeltaRValueMapProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
