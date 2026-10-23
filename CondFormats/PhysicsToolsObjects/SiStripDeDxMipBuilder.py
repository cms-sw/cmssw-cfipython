import FWCore.ParameterSet.Config as cms

def SiStripDeDxMipBuilder(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripDeDxMipBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
