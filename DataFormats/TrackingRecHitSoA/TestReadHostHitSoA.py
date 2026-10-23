import FWCore.ParameterSet.Config as cms

def TestReadHostHitSoA(*args, **kwargs):
  mod = cms.EDAnalyzer('TestReadHostHitSoA',
    input = cms.required.InputTag,
    hitSize = cms.uint32(1000),
    offsetBPIX2 = cms.uint32(50),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
