import FWCore.ParameterSet.Config as cms

EvFDaqDirector = cms.Service('EvFDaqDirector',
  baseDir = cms.untracked.string('.'),
  buBaseDir = cms.untracked.string('.'),
  runNumber = cms.untracked.uint32(0),
  useFileBroker = cms.untracked.bool(False),
  fileBrokerHost = cms.untracked.string(''),
  fileBrokerPort = cms.untracked.string('8080'),
  fileBrokerKeepAlive = cms.untracked.bool(True),
  fileBrokerUseLocalLock = cms.untracked.bool(True),
  outputAdler32Recheck = cms.untracked.bool(False),
  requireTransfersPSet = cms.untracked.bool(False),
  selectedTransferMode = cms.untracked.string(''),
  fuLockPollInterval = cms.untracked.uint32(2000),
  mergingPset = cms.untracked.string('')
)
