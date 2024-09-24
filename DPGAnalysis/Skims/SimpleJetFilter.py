import FWCore.ParameterSet.Config as cms

def SimpleJetFilter(*args, **kwargs):
  mod = cms.EDFilter('SimpleJetFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod