import FWCore.ParameterSet.Config as cms

def CrystalCenterDump(*args, **kwargs):
  mod = cms.EDAnalyzer('CrystalCenterDump',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
