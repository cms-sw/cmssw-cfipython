import FWCore.ParameterSet.Config as cms

def ZombieKillerService(*args, **kwargs):
  mod = cms.Service('ZombieKillerService',
    secondsBetweenChecks = cms.untracked.uint32(60),
    numberOfAllowedFailedChecksInARow = cms.untracked.uint32(3)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
