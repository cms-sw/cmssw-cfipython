import FWCore.ParameterSet.Config as cms

thingProd = cms.EDProducer('ThingProducer',
  offsetDelta = cms.int32(0),
  noPut = cms.untracked.bool(False)
)
