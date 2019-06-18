import FWCore.ParameterSet.Config as cms

AdaptorConfig = cms.Service('AdaptorConfig',
  enable = cms.optional.untracked.bool,
  stats = cms.optional.untracked.bool,
  cacheHint = cms.optional.untracked.string,
  readHint = cms.optional.untracked.string,
  tempDir = cms.optional.untracked.string,
  tempMinFree = cms.optional.untracked.double,
  native = cms.optional.untracked.vstring
)
