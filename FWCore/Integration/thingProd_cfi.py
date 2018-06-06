import FWCore.ParameterSet.Config as cms

thingProd = cms.EDProducer('ThingProducer',
  offsetDelta = cms.int32(0),
  nThings = cms.int32(20),
  noPut = cms.untracked.bool(False)
)
