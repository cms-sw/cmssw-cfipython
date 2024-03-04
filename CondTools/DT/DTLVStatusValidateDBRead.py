import FWCore.ParameterSet.Config as cms

def DTLVStatusValidateDBRead(**kwargs):
  mod = cms.EDAnalyzer('DTLVStatusValidateDBRead',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
