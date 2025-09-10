import FWCore.ParameterSet.Config as cms

def TestReadHostHitSoA(*args, **kwargs):
  mod = cms.EDAnalyzer('TestReadHostHitSoA',
    input = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
