import FWCore.ParameterSet.Config as cms

def StallMonitor(*args, **kwargs):
  mod = cms.Service('StallMonitor',
    fileName = cms.untracked.string(''),
    stallThreshold = cms.untracked.double(0.1),
    recordFrameworkTransitions = cms.untracked.bool(False)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
