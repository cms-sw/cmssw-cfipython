import FWCore.ParameterSet.Config as cms

def PatZjetsJetAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('PatZjetsJetAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
