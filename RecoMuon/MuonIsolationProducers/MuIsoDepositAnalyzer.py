import FWCore.ParameterSet.Config as cms

def MuIsoDepositAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('MuIsoDepositAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
