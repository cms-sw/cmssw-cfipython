import FWCore.ParameterSet.Config as cms

def TrackingVertexCategorySelector(*args, **kwargs):
  mod = cms.EDFilter('TrackingVertexCategorySelector',
    src = cms.InputTag(''),
    cut = cms.string(''),
    trackingTruth = cms.untracked.InputTag('mix', 'MergedTrackTruth'),
    vertexAssociator = cms.untracked.InputTag('vertexAssociatorByTracksByHits'),
    bestMatchByMaxValue = cms.untracked.bool(True),
    enableRecoToSim = cms.untracked.bool(True),
    enableSimToReco = cms.untracked.bool(False),
    hepMC = cms.untracked.InputTag('generatorSmeared'),
    longLivedDecayLength = cms.untracked.double(1e-14),
    vertexClusteringDistance = cms.untracked.double(0.003),
    filter = cms.bool(False),
    throwOnMissing = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
