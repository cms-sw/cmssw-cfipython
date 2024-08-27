import FWCore.ParameterSet.Config as cms

def EEBadScFilter(**kwargs):
  mod = cms.EDFilter('EEBadScFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
