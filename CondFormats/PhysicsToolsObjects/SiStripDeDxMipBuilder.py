import FWCore.ParameterSet.Config as cms

def SiStripDeDxMipBuilder(**kwargs):
  mod = cms.EDAnalyzer('SiStripDeDxMipBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
