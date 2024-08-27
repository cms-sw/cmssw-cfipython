import FWCore.ParameterSet.Config as cms

def PFMuonDQMAnalyzer(**kwargs):
  mod = cms.EDProducer('PFMuonDQMAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
