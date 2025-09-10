import FWCore.ParameterSet.Config as cms

def TestAlpakaObjectAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('TestAlpakaObjectAnalyzer',
    source = cms.required.InputTag,
    expectBackend = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
