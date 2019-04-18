import FWCore.ParameterSet.Config as cms

l1tRawToDigi = cms.EDProducer('L1TRawToDigi',
  FedIds = cms.vint32(),
  Setup = cms.string(''),
  FWId = cms.uint32(0),
  FWOverride = cms.bool(False),
  CTP7 = cms.untracked.bool(False),
  MTF7 = cms.untracked.bool(False),
  InputLabel = cms.InputTag('rawDataCollector'),
  lenSlinkHeader = cms.untracked.int32(8),
  lenSlinkTrailer = cms.untracked.int32(8),
  lenAMCHeader = cms.untracked.int32(8),
  lenAMCTrailer = cms.untracked.int32(0),
  lenAMC13Header = cms.untracked.int32(8),
  lenAMC13Trailer = cms.untracked.int32(8),
  debug = cms.untracked.bool(False),
  MinFeds = cms.uint32(0)
)
