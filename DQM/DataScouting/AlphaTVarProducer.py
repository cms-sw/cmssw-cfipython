import FWCore.ParameterSet.Config as cms

def AlphaTVarProducer(*args, **kwargs):
  mod = cms.EDProducer('AlphaTVarProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
