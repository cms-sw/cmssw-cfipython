import FWCore.ParameterSet.Config as cms

def ZombieKillerService(**kwargs):
  mod = cms.Service('ZombieKillerService',
    secondsBetweenChecks = cms.untracked.uint32(60),
    numberOfAllowedFailedChecksInARow = cms.untracked.uint32(3)
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
