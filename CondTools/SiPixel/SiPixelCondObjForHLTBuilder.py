import FWCore.ParameterSet.Config as cms

def SiPixelCondObjForHLTBuilder(**kwargs):
  mod = cms.EDAnalyzer('SiPixelCondObjForHLTBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
