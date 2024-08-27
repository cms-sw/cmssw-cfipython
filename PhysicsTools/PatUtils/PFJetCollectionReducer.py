import FWCore.ParameterSet.Config as cms

def PFJetCollectionReducer(**kwargs):
  mod = cms.EDProducer('PFJetCollectionReducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
