import FWCore.ParameterSet.Config as cms

def CaloMETShallowCloneProducer(**kwargs):
  mod = cms.EDProducer('CaloMETShallowCloneProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod