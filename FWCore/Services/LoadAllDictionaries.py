import FWCore.ParameterSet.Config as cms

def LoadAllDictionaries(*args, **kwargs):
  mod = cms.Service('LoadAllDictionaries',
    doLoad = cms.untracked.bool(True)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
