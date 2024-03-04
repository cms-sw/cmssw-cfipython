import FWCore.ParameterSet.Config as cms

def SiPixelCondObjBuilder(**kwargs):
  mod = cms.EDAnalyzer('SiPixelCondObjBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
