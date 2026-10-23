import FWCore.ParameterSet.Config as cms

def TestReadHostTrackSoA(*args, **kwargs):
  mod = cms.EDAnalyzer('TestReadHostTrackSoA',
    input = cms.required.InputTag,
    trackSize = cms.uint32(1000),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
