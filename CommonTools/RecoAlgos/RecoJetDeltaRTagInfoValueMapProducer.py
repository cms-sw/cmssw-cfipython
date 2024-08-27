import FWCore.ParameterSet.Config as cms

def RecoJetDeltaRTagInfoValueMapProducer(**kwargs):
  mod = cms.EDProducer('RecoJetDeltaRTagInfoValueMapProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
