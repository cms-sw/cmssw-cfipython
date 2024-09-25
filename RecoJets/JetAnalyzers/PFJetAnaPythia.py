import FWCore.ParameterSet.Config as cms

def PFJetAnaPythia(*args, **kwargs):
  mod = cms.EDAnalyzer('PFJetAnaPythia',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
