import FWCore.ParameterSet.Config as cms

def edmtest_one_SharedResourcesFilter(**kwargs):
  mod = cms.EDFilter('edmtest::one::SharedResourcesFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
