import FWCore.ParameterSet.Config as cms

def edmtest_one_InputProcessBlockIntFilter(**kwargs):
  mod = cms.EDFilter('edmtest::one::InputProcessBlockIntFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
