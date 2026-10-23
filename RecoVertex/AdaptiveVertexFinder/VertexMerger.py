import FWCore.ParameterSet.Config as cms

def VertexMerger(*args, **kwargs):
  mod = cms.EDProducer('VertexMerger',
    maxFraction = cms.double(0.7),
    minSignificance = cms.double(2),
    secondaryVertices = cms.InputTag('inclusiveVertexFinder'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
