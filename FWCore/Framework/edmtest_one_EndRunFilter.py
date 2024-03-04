import FWCore.ParameterSet.Config as cms

def edmtest_one_EndRunFilter(**kwargs):
  mod = cms.EDFilter('edmtest::one::EndRunFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
