import FWCore.ParameterSet.Config as cms

def ExampleMuonAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ExampleMuonAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
