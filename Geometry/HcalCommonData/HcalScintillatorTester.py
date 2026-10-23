import FWCore.ParameterSet.Config as cms

def HcalScintillatorTester(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalScintillatorTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
