import FWCore.ParameterSet.Config as cms

def TestAlpakaObjectAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('TestAlpakaObjectAnalyzer',
    source = cms.required.InputTag,
    expectBackend = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
