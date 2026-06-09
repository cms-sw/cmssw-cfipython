import FWCore.ParameterSet.Config as cms

def HcalInterpolatedPulseMapDBReader(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalInterpolatedPulseMapDBReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
