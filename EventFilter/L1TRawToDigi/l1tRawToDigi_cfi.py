import FWCore.ParameterSet.Config as cms

l1tRawToDigi = cms.EDProducer('L1TRawToDigi',
  FWId = cms.uint32(4294967295),
  FWOverride = cms.bool(False),
  CTP7 = cms.untracked.bool(False),
  InputLabel = cms.InputTag('rawDataCollector'),
  FedIds = cms.vint32(),
  Setup = cms.string(''),
  lenSlinkHeader = cms.untracked.int32(8),
  lenSlinkTrailer = cms.untracked.int32(8),
  lenAMCHeader = cms.untracked.int32(8),
  lenAMCTrailer = cms.untracked.int32(0),
  lenAMC13Header = cms.untracked.int32(8),
  lenAMC13Trailer = cms.untracked.int32(8),
  debug = cms.untracked.bool(False)
)
