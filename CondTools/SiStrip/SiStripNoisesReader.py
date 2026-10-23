import FWCore.ParameterSet.Config as cms

def SiStripNoisesReader(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripNoisesReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
