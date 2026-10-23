import FWCore.ParameterSet.Config as cms

def DTLVStatusValidateDBWrite(*args, **kwargs):
  mod = cms.EDAnalyzer('DTLVStatusValidateDBWrite',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
