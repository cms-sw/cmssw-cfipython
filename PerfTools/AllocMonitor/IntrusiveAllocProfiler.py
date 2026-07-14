import FWCore.ParameterSet.Config as cms

def IntrusiveAllocProfiler(*args, **kwargs):
  mod = cms.Service('IntrusiveAllocProfiler',
    filePattern = cms.untracked.string(''),
    statistics = cms.untracked.bool(False),
    deallocationReport = cms.untracked.bool(True),
    churnReport = cms.untracked.bool(True)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
