import FWCore.ParameterSet.Config as cms

def L1GlobalTriggerRawToDigi(**kwargs):
  mod = cms.EDProducer('L1GlobalTriggerRawToDigi',
    DaqGtInputTag = cms.InputTag('l1GtPack'),
    DaqGtFedId = cms.untracked.int32(813),
    ActiveBoardsMask = cms.uint32(65535),
    UnpackBxInEvent = cms.int32(-1),
    Verbosity = cms.untracked.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
