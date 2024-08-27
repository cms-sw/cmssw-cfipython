import FWCore.ParameterSet.Config as cms

def CaloJetShallowCloneProducer(**kwargs):
  mod = cms.EDProducer('CaloJetShallowCloneProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
