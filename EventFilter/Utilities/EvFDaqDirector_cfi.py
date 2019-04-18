import FWCore.ParameterSet.Config as cms

EvFDaqDirector = cms.Service('EvFDaqDirector',
  baseDir = cms.untracked.string('.'),
  buBaseDir = cms.untracked.string('.'),
  runNumber = cms.untracked.uint32(0),
  outputAdler32Recheck = cms.untracked.bool(False),
  requireTransfersPSet = cms.untracked.bool(False),
  selectedTransferMode = cms.untracked.string(''),
  fuLockPollInterval = cms.untracked.uint32(2000),
  emptyLumisectionMode = cms.untracked.bool(True),
  microMergeDisabled = cms.untracked.bool(True),
  mergingPset = cms.untracked.string('')
)
