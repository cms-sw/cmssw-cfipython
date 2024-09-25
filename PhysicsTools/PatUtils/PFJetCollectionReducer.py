import FWCore.ParameterSet.Config as cms

def PFJetCollectionReducer(*args, **kwargs):
  mod = cms.EDProducer('PFJetCollectionReducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
