import FWCore.ParameterSet.Config as cms

def DTPhiLutTester(*args, **kwargs):
  mod = cms.EDAnalyzer('DTPhiLutTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
