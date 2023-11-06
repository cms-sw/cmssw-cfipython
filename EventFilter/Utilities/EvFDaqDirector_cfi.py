import FWCore.ParameterSet.Config as cms

EvFDaqDirector = cms.Service('EvFDaqDirector',
  baseDir = cms.untracked.string('.'),
  buBaseDir = cms.untracked.string('.'),
  buBaseDirsAll = cms.untracked.vstring(),
  runNumber = cms.untracked.uint32(0),
  useFileBroker = cms.untracked.bool(False),
  fileBrokerHostFromCfg = cms.untracked.bool(True),
  fileBrokerHost = cms.untracked.string('InValid'),
  fileBrokerPort = cms.untracked.string('8080'),
  fileBrokerKeepAlive = cms.untracked.bool(True),
  fileBrokerUseLocalLock = cms.untracked.bool(True),
  fuLockPollInterval = cms.untracked.uint32(2000),
  outputAdler32Recheck = cms.untracked.bool(False),
  requireTransfersPSet = cms.untracked.bool(False),
  selectedTransferMode = cms.untracked.string(''),
  directorIsBU = cms.untracked.bool(False),
  hltSourceDirectory = cms.untracked.string(''),
  mergingPset = cms.untracked.string('')
)
