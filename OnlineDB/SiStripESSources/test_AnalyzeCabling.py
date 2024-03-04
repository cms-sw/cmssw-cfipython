import FWCore.ParameterSet.Config as cms

def test_AnalyzeCabling(**kwargs):
  mod = cms.EDAnalyzer('test_AnalyzeCabling',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
