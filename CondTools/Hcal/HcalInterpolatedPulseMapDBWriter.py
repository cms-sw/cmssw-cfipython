import FWCore.ParameterSet.Config as cms

def HcalInterpolatedPulseMapDBWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalInterpolatedPulseMapDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
