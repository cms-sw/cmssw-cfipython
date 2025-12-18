import FWCore.ParameterSet.Config as cms

def FailingGeneratorFilter(*args, **kwargs):
  mod = cms.EDFilter('FailingGeneratorFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
