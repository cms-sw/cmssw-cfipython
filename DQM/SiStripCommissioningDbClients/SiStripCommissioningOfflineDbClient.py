import FWCore.ParameterSet.Config as cms

def SiStripCommissioningOfflineDbClient(**kwargs):
  mod = cms.EDAnalyzer('SiStripCommissioningOfflineDbClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
