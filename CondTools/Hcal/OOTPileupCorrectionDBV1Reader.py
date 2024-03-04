import FWCore.ParameterSet.Config as cms

def OOTPileupCorrectionDBV1Reader(**kwargs):
  mod = cms.EDAnalyzer('OOTPileupCorrectionDBV1Reader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
