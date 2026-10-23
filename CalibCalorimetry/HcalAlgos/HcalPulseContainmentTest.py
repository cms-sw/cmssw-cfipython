import FWCore.ParameterSet.Config as cms

def HcalPulseContainmentTest(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalPulseContainmentTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
