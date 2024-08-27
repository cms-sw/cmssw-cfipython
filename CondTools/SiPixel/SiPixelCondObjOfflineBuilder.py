import FWCore.ParameterSet.Config as cms

def SiPixelCondObjOfflineBuilder(**kwargs):
  mod = cms.EDAnalyzer('SiPixelCondObjOfflineBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
