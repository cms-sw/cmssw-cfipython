import FWCore.ParameterSet.Config as cms

def LHEPtFilter(*args, **kwargs):
  mod = cms.EDFilter('LHEPtFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
