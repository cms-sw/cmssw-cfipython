import FWCore.ParameterSet.Config as cms

def FastSimDataFilter(*args, **kwargs):
  mod = cms.EDFilter('FastSimDataFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
