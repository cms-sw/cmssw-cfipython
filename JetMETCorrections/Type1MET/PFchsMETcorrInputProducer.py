import FWCore.ParameterSet.Config as cms

def PFchsMETcorrInputProducer(**kwargs):
  mod = cms.EDProducer('PFchsMETcorrInputProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
