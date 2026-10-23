import FWCore.ParameterSet.Config as cms

def ThingProducer(*args, **kwargs):
  mod = cms.EDProducer('ThingProducer',
    offsetDelta = cms.int32(0),
    nThings = cms.int32(20),
    grow = cms.bool(False),
    noPut = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
