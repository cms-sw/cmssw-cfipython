import FWCore.ParameterSet.Config as cms

def HLTVertexFilter(**kwargs):
  mod = cms.EDFilter('HLTVertexFilter',
    saveTags = cms.bool(True),
    inputTag = cms.InputTag('hltPixelVertices'),
    minNDoF = cms.double(0),
    maxChi2 = cms.double(99999),
    maxD0 = cms.double(1),
    maxZ = cms.double(15),
    minVertices = cms.uint32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
