import FWCore.ParameterSet.Config as cms

def WrappedEDMuonAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('WrappedEDMuonAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
