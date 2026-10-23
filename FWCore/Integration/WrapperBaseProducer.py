import FWCore.ParameterSet.Config as cms

def WrapperBaseProducer(*args, **kwargs):
  mod = cms.EDProducer('WrapperBaseProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
