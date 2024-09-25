import FWCore.ParameterSet.Config as cms

def SiStripPedestalsReader(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripPedestalsReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
