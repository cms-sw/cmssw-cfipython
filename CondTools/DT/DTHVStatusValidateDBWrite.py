import FWCore.ParameterSet.Config as cms

def DTHVStatusValidateDBWrite(**kwargs):
  mod = cms.EDAnalyzer('DTHVStatusValidateDBWrite',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
