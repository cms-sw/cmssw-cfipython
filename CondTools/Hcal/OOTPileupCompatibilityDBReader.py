import FWCore.ParameterSet.Config as cms

def OOTPileupCompatibilityDBReader(*args, **kwargs):
  mod = cms.EDAnalyzer('OOTPileupCompatibilityDBReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
