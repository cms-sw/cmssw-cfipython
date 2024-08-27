import FWCore.ParameterSet.Config as cms

def test_Template(**kwargs):
  mod = cms.EDAnalyzer('test_Template',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
