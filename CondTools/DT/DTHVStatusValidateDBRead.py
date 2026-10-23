import FWCore.ParameterSet.Config as cms

def DTHVStatusValidateDBRead(*args, **kwargs):
  mod = cms.EDAnalyzer('DTHVStatusValidateDBRead',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
