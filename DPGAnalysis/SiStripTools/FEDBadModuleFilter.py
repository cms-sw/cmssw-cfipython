import FWCore.ParameterSet.Config as cms

def FEDBadModuleFilter(**kwargs):
  mod = cms.EDFilter('FEDBadModuleFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
