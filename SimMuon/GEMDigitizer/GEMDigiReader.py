import FWCore.ParameterSet.Config as cms

def GEMDigiReader(*args, **kwargs):
  mod = cms.EDAnalyzer('GEMDigiReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
