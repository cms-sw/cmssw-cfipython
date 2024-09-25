import FWCore.ParameterSet.Config as cms

def GenMETShallowCloneProducer(*args, **kwargs):
  mod = cms.EDProducer('GenMETShallowCloneProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
