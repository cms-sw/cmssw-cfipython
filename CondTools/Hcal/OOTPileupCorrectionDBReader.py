import FWCore.ParameterSet.Config as cms

def OOTPileupCorrectionDBReader(*args, **kwargs):
  mod = cms.EDAnalyzer('OOTPileupCorrectionDBReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
