import FWCore.ParameterSet.Config as cms

def SiStripCommissioningOfflineDbClient(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripCommissioningOfflineDbClient',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
