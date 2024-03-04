import FWCore.ParameterSet.Config as cms

def MuonPFAnalyzer(**kwargs):
  mod = cms.EDProducer('MuonPFAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
