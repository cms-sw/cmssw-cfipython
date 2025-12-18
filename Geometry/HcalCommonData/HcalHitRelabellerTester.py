import FWCore.ParameterSet.Config as cms

def HcalHitRelabellerTester(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalHitRelabellerTester',
    neutralDensity = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
