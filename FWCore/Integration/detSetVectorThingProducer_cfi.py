import FWCore.ParameterSet.Config as cms

detSetVectorThingProducer = cms.EDProducer('DetSetVectorThingProducer',
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
