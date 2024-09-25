import FWCore.ParameterSet.Config as cms

def MuIsoDepositAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('MuIsoDepositAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
