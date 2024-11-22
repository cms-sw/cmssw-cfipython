import FWCore.ParameterSet.Config as cms

def DetSetVectorThingProducer(*args, **kwargs):
  mod = cms.EDProducer('DetSetVectorThingProducer',
    offsetDelta = cms.int32(0),
    detSets = cms.vint32(
      1,
      2,
      3
    ),
    nThings = cms.int32(20),
    grow = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
