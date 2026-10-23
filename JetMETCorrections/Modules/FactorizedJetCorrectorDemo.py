import FWCore.ParameterSet.Config as cms

def FactorizedJetCorrectorDemo(*args, **kwargs):
  mod = cms.EDAnalyzer('FactorizedJetCorrectorDemo',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
