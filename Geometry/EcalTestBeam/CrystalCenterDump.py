import FWCore.ParameterSet.Config as cms

def CrystalCenterDump(**kwargs):
  mod = cms.EDAnalyzer('CrystalCenterDump',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
