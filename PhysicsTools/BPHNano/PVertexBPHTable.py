import FWCore.ParameterSet.Config as cms

def PVertexBPHTable(*args, **kwargs):
  mod = cms.EDProducer('PVertexBPHTable',
    pvSrc = cms.required.InputTag,
    dileptons = cms.required.InputTag,
    maxDzDilep = cms.required.double,
    goodPvCut = cms.required.string,
    pvName = cms.required.string,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
