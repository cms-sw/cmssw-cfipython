import FWCore.ParameterSet.Config as cms

def DTHVStatusValidateDBRead(**kwargs):
  mod = cms.EDAnalyzer('DTHVStatusValidateDBRead',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
