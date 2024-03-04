import FWCore.ParameterSet.Config as cms

def LoadAllDictionaries(**kwargs):
  mod = cms.Service('LoadAllDictionaries',
    doLoad = cms.untracked.bool(True)
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
