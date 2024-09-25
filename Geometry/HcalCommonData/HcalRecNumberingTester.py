import FWCore.ParameterSet.Config as cms

def HcalRecNumberingTester(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalRecNumberingTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
