import FWCore.ParameterSet.Config as cms

def TagProbeMassEDMFilter(**kwargs):
  mod = cms.EDFilter('TagProbeMassEDMFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
