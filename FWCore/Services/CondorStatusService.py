import FWCore.ParameterSet.Config as cms

def CondorStatusService(**kwargs):
  mod = cms.Service('CondorStatusService',
    updateIntervalSeconds = cms.untracked.uint32(180),
    debug = cms.untracked.bool(False),
    EMAInterval = cms.untracked.double(900),
    tag = cms.optional.untracked.string,
    enable = cms.untracked.bool(True)
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
