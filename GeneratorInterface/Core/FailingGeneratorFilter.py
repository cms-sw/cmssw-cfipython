import FWCore.ParameterSet.Config as cms

def FailingGeneratorFilter(**kwargs):
  mod = cms.EDFilter('FailingGeneratorFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
