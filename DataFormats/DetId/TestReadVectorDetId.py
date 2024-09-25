import FWCore.ParameterSet.Config as cms

def TestReadVectorDetId(*args, **kwargs):
  mod = cms.EDAnalyzer('TestReadVectorDetId',
    expectedTestValue = cms.required.uint32,
    collectionTag = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
