import FWCore.ParameterSet.Config as cms

def TestAlpakaAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('TestAlpakaAnalyzer',
    source = cms.required.InputTag,
    expectSize = cms.int32(-1),
    expectXvalues = cms.vdouble(),
    expectBackend = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
