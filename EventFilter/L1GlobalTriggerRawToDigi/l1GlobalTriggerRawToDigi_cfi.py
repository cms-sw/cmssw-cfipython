import FWCore.ParameterSet.Config as cms

l1GlobalTriggerRawToDigi = cms.EDProducer('L1GlobalTriggerRawToDigi',
  DaqGtInputTag = cms.InputTag('l1GtPack'),
  DaqGtFedId = cms.untracked.int32(813),
  ActiveBoardsMask = cms.uint32(65535),
  UnpackBxInEvent = cms.int32(-1),
  Verbosity = cms.untracked.int32(0)
)
