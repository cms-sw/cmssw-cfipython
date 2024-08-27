import FWCore.ParameterSet.Config as cms

def ThingProducer(**kwargs):
  mod = cms.EDProducer('ThingProducer',
    offsetDelta = cms.int32(0),
    nThings = cms.int32(20),
    grow = cms.bool(False),
    noPut = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
