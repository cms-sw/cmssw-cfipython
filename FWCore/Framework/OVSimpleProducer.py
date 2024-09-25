import FWCore.ParameterSet.Config as cms

def OVSimpleProducer(*args, **kwargs):
  mod = cms.EDProducer('OVSimpleProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
