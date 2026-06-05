import FWCore.ParameterSet.Config as cms

def PatZjetsJetAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('PatZjetsJetAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
