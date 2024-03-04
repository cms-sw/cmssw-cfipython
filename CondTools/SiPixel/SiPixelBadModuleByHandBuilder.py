import FWCore.ParameterSet.Config as cms

def SiPixelBadModuleByHandBuilder(**kwargs):
  mod = cms.EDAnalyzer('SiPixelBadModuleByHandBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
