import FWCore.ParameterSet.Config as cms

ZombieKillerService = cms.Service('ZombieKillerService',
  secondsBetweenChecks = cms.untracked.uint32(60),
  numberOfAllowedFailedChecksInARow = cms.untracked.uint32(3)
)
