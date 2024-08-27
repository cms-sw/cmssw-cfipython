import FWCore.ParameterSet.Config as cms

def XrdStatisticsService(**kwargs):
  mod = cms.Service('XrdStatisticsService',
    reportToFJR = cms.untracked.bool(True)
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
