import FWCore.ParameterSet.Config as cms

FixMissingStreamerInfos = cms.Service('FixMissingStreamerInfos',
  fileInPath = cms.required.untracked.FileInPath
)
