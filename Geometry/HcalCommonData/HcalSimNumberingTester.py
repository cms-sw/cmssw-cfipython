import FWCore.ParameterSet.Config as cms

def HcalSimNumberingTester(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalSimNumberingTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
