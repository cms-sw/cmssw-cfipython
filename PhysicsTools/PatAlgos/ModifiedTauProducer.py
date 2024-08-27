import FWCore.ParameterSet.Config as cms

def ModifiedTauProducer(**kwargs):
  mod = cms.EDProducer('ModifiedTauProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
