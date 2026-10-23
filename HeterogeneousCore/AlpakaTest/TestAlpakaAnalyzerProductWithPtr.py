import FWCore.ParameterSet.Config as cms

def TestAlpakaAnalyzerProductWithPtr(*args, **kwargs):
  mod = cms.EDAnalyzer('TestAlpakaAnalyzerProductWithPtr',
    src = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
