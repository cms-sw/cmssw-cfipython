import FWCore.ParameterSet.Config as cms

def TPStubValueMapProducer(*args, **kwargs):
  mod = cms.EDProducer('TPStubValueMapProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
