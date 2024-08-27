import FWCore.ParameterSet.Config as cms

def HerwigMaxPtPartonFilter(**kwargs):
  mod = cms.EDFilter('HerwigMaxPtPartonFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
