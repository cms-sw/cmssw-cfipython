import FWCore.ParameterSet.Config as cms

def HcalInterpolatedPulseDBReader(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalInterpolatedPulseDBReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
