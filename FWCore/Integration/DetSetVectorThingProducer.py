import FWCore.ParameterSet.Config as cms

def DetSetVectorThingProducer(**kwargs):
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
