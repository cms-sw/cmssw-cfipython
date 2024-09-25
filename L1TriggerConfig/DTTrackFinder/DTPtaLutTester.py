import FWCore.ParameterSet.Config as cms

def DTPtaLutTester(*args, **kwargs):
  mod = cms.EDAnalyzer('DTPtaLutTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
