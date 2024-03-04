import FWCore.ParameterSet.Config as cms

def ZElectronsSelectorAndSkim(**kwargs):
  mod = cms.EDFilter('ZElectronsSelectorAndSkim',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
