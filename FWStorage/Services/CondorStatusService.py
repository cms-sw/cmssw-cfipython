import FWCore.ParameterSet.Config as cms

def CondorStatusService(*args, **kwargs):
  mod = cms.Service('CondorStatusService',
    updateIntervalSeconds = cms.untracked.uint32(180),
    debug = cms.untracked.bool(False),
    EMAInterval = cms.untracked.double(900),
    tag = cms.optional.untracked.string,
    enable = cms.untracked.bool(True)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
