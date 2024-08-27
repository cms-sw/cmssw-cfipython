import FWCore.ParameterSet.Config as cms

def MuonEnergyDepositAnalyzer(**kwargs):
  mod = cms.EDProducer('MuonEnergyDepositAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
