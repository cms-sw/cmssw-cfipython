import FWCore.ParameterSet.Config as cms

def VSimpleProducer(*args, **kwargs):
  mod = cms.EDProducer('VSimpleProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
