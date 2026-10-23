import FWCore.ParameterSet.Config as cms

def GenJetAnaPythia(*args, **kwargs):
  mod = cms.EDAnalyzer('GenJetAnaPythia',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
