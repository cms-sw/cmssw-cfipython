import FWCore.ParameterSet.Config as cms

def XrdStatisticsService(*args, **kwargs):
  mod = cms.Service('XrdStatisticsService',
    reportToFJR = cms.untracked.bool(True)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
