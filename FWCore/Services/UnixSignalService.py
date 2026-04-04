import FWCore.ParameterSet.Config as cms

def UnixSignalService(*args, **kwargs):
  mod = cms.Service('UnixSignalService',
    EnableCtrlC = cms.untracked.bool(True)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
