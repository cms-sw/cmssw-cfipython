import FWCore.ParameterSet.Config as cms

def DTLVStatusValidateDBRead(*args, **kwargs):
  mod = cms.EDAnalyzer('DTLVStatusValidateDBRead',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
