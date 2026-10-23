import FWCore.ParameterSet.Config as cms

def HcalTestNumberingTester(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalTestNumberingTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
