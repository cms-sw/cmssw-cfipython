import FWCore.ParameterSet.Config as cms

def TagProbeMassEDMFilter(*args, **kwargs):
  mod = cms.EDFilter('TagProbeMassEDMFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
