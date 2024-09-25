import FWCore.ParameterSet.Config as cms

def PVSSIDReader(*args, **kwargs):
  mod = cms.EDAnalyzer('PVSSIDReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
