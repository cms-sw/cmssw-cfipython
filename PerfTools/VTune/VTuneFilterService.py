import FWCore.ParameterSet.Config as cms

def VTuneFilterService(*args, **kwargs):
  mod = cms.Service('VTuneFilterService',
    moduleNames = cms.untracked.vstring(),
    allModules = cms.untracked.bool(False)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
