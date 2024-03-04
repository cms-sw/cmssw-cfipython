import FWCore.ParameterSet.Config as cms

def BooleanFilter(**kwargs):
  mod = cms.EDFilter('BooleanFilter',
    src = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
