import FWCore.ParameterSet.Config as cms

def CaloMETShallowCloneProducer(*args, **kwargs):
  mod = cms.EDProducer('CaloMETShallowCloneProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
