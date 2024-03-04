import FWCore.ParameterSet.Config as cms

def StallMonitor(**kwargs):
  mod = cms.Service('StallMonitor',
    fileName = cms.untracked.string(''),
    stallThreshold = cms.untracked.double(0.1),
    recordFrameworkTransitions = cms.untracked.bool(False)
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
