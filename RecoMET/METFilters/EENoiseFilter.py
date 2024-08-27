import FWCore.ParameterSet.Config as cms

def EENoiseFilter(**kwargs):
  mod = cms.EDFilter('EENoiseFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
