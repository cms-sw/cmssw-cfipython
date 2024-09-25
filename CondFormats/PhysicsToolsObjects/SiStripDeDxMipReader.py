import FWCore.ParameterSet.Config as cms

def SiStripDeDxMipReader(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripDeDxMipReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
