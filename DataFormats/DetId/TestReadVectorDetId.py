import FWCore.ParameterSet.Config as cms

def TestReadVectorDetId(**kwargs):
  mod = cms.EDAnalyzer('TestReadVectorDetId',
    expectedTestValue = cms.required.uint32,
    collectionTag = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
