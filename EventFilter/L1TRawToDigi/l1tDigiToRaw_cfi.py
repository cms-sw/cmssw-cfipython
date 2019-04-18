import FWCore.ParameterSet.Config as cms

l1tDigiToRaw = cms.EDProducer('L1TDigiToRaw',
  FWId = cms.uint32(4294967295),
  eventType = cms.untracked.int32(1),
  InputLabel = cms.InputTag(''),
  lenSlinkHeader = cms.untracked.int32(8),
  lenSlinkTrailer = cms.untracked.int32(8)
)
