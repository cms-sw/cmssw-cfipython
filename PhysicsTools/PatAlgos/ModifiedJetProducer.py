import FWCore.ParameterSet.Config as cms

def ModifiedJetProducer(**kwargs):
  mod = cms.EDProducer('ModifiedJetProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
