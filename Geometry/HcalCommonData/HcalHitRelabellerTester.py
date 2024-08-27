import FWCore.ParameterSet.Config as cms

def HcalHitRelabellerTester(**kwargs):
  mod = cms.EDAnalyzer('HcalHitRelabellerTester',
    neutralDensity = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
