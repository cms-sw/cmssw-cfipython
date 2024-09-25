import FWCore.ParameterSet.Config as cms

def FastMonitoringService(*args, **kwargs):
  mod = cms.Service('FastMonitoringService',
    tbbMonitoringMode = cms.untracked.bool(True),
    tbbConcurrencyTracker = cms.untracked.bool(True),
    sleepTime = cms.untracked.int32(1),
    fastMonIntervals = cms.untracked.uint32(2),
    filePerFwkStream = cms.untracked.bool(True),
    verbose = cms.untracked.bool(False)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
