import FWCore.ParameterSet.Config as cms

def Timing(*args, **kwargs):
  mod = cms.Service('Timing',
    summaryOnly = cms.untracked.bool(False),
    useJobReport = cms.untracked.bool(True),
    excessiveTimeThreshold = cms.untracked.double(0)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
