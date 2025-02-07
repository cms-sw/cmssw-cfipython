import FWCore.ParameterSet.Config as cms

def OOTPileupCorrectionDBV1Writer(*args, **kwargs):
  mod = cms.EDAnalyzer('OOTPileupCorrectionDBV1Writer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
