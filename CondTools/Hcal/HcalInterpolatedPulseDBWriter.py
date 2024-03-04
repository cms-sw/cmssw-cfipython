import FWCore.ParameterSet.Config as cms

def HcalInterpolatedPulseDBWriter(**kwargs):
  mod = cms.EDAnalyzer('HcalInterpolatedPulseDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
