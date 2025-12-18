import FWCore.ParameterSet.Config as cms

def OOTPileupCorrectionDBWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('OOTPileupCorrectionDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
