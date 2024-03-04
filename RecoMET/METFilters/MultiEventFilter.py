import FWCore.ParameterSet.Config as cms

def MultiEventFilter(**kwargs):
  mod = cms.EDFilter('MultiEventFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
