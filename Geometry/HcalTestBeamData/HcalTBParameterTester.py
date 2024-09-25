import FWCore.ParameterSet.Config as cms

def HcalTBParameterTester(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalTBParameterTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
