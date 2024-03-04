import FWCore.ParameterSet.Config as cms

def RecoJetToPatJetDeltaRValueMapProducer(**kwargs):
  mod = cms.EDProducer('RecoJetToPatJetDeltaRValueMapProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
