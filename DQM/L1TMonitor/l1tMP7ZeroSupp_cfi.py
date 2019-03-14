import FWCore.ParameterSet.Config as cms

l1tMP7ZeroSupp = cms.EDAnalyzer('L1TMP7ZeroSupp',
  zsEnabled = cms.untracked.bool(True),
  lenSlinkHeader = cms.untracked.int32(8),
  lenSlinkTrailer = cms.untracked.int32(8),
  lenAMC13Header = cms.untracked.int32(8),
  lenAMC13Trailer = cms.untracked.int32(8),
  lenAMCHeader = cms.untracked.int32(8),
  lenAMCTrailer = cms.untracked.int32(0),
  zsFlagMask = cms.untracked.int32(1),
  newZsFlagMask = cms.untracked.int32(2),
  dataInvFlagMask = cms.untracked.int32(1),
  maxFEDReadoutSize = cms.untracked.int32(10000),
  monitorDir = cms.untracked.string(''),
  verbose = cms.untracked.bool(False)
)
