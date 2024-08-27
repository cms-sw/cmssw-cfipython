import FWCore.ParameterSet.Config as cms

def SiPixelBadModuleReader(**kwargs):
  mod = cms.EDAnalyzer('SiPixelBadModuleReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
