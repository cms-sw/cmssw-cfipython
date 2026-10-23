import FWCore.ParameterSet.Config as cms

def BsJpsiPhiFilter(*args, **kwargs):
  mod = cms.EDFilter('BsJpsiPhiFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
