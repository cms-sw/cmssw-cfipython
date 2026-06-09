import FWCore.ParameterSet.Config as cms

def TestAlpakaAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('TestAlpakaAnalyzer',
    source = cms.required.InputTag,
    expectSize = cms.int32(-1),
    expectXvalues = cms.vdouble(),
    expectBackend = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
