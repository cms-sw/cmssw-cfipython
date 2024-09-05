import FWCore.ParameterSet.Config as cms

def TestAlpakaAnalyzerProductWithPtr(**kwargs):
  mod = cms.EDAnalyzer('TestAlpakaAnalyzerProductWithPtr',
    src = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
