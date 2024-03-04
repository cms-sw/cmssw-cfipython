import FWCore.ParameterSet.Config as cms

def SiStripCommissioningOfflineClient(**kwargs):
  mod = cms.EDAnalyzer('SiStripCommissioningOfflineClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
