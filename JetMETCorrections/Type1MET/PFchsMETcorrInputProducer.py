import FWCore.ParameterSet.Config as cms

def PFchsMETcorrInputProducer(*args, **kwargs):
  mod = cms.EDProducer('PFchsMETcorrInputProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
