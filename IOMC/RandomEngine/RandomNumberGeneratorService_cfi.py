import FWCore.ParameterSet.Config as cms

RandomNumberGeneratorService = cms.Service('RandomNumberGeneratorService',
  restoreStateTag = cms.untracked.InputTag(''),
  saveFileName = cms.untracked.string(''),
  restoreFileName = cms.untracked.string(''),
  enableChecking = cms.untracked.bool(False),
  eventSeedOffset = cms.untracked.uint32(0),
  verbose = cms.untracked.bool(False)
)
