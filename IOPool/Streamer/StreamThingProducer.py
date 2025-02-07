import FWCore.ParameterSet.Config as cms

def StreamThingProducer(*args, **kwargs):
  mod = cms.EDProducer('StreamThingProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
