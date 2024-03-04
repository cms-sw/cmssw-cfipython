import FWCore.ParameterSet.Config as cms

def trgMatchedJetProducer(**kwargs):
  mod = cms.EDProducer('trgMatchedJetProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
