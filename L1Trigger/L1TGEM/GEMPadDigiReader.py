import FWCore.ParameterSet.Config as cms

def GEMPadDigiReader(*args, **kwargs):
  mod = cms.EDAnalyzer('GEMPadDigiReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
