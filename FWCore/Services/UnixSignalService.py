import FWCore.ParameterSet.Config as cms

def UnixSignalService(**kwargs):
  mod = cms.Service('UnixSignalService',
    EnableCtrlC = cms.untracked.bool(True)
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
