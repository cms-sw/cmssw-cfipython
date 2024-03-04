import FWCore.ParameterSet.Config as cms

def FastSimDataFilter(**kwargs):
  mod = cms.EDFilter('FastSimDataFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
