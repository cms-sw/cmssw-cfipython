import FWCore.ParameterSet.Config as cms

def Timing(**kwargs):
  mod = cms.Service('Timing',
    summaryOnly = cms.untracked.bool(False),
    useJobReport = cms.untracked.bool(True),
    excessiveTimeThreshold = cms.untracked.double(0)
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
