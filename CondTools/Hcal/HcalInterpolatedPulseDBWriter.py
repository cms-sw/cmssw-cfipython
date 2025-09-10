import FWCore.ParameterSet.Config as cms

def HcalInterpolatedPulseDBWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalInterpolatedPulseDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
