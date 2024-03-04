import FWCore.ParameterSet.Config as cms

def UnitTestClient_Nd(**kwargs):
  mod = cms.EDAnalyzer('UnitTestClient_Nd',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
