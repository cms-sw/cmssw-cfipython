import FWCore.ParameterSet.Config as cms

def HerwigMaxPtPartonFilter(*args, **kwargs):
  mod = cms.EDFilter('HerwigMaxPtPartonFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
