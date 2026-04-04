import FWCore.ParameterSet.Config as cms

def SiStripCommissioningOfflineClient(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripCommissioningOfflineClient',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
