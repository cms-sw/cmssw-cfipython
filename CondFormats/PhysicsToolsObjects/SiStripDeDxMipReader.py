import FWCore.ParameterSet.Config as cms

def SiStripDeDxMipReader(**kwargs):
  mod = cms.EDAnalyzer('SiStripDeDxMipReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
