import FWCore.ParameterSet.Config as cms

def BranchTracksterRecoValidator(*args, **kwargs):
  mod = cms.EDProducer('BranchTracksterRecoValidator',
    src = cms.InputTag('truthLogicalGraphProducer'),
    hitIndex = cms.InputTag('truthLogicalGraphHitIndexProducer'),
    interestingPdgIds = cms.vint32(),
    folder = cms.string('BranchValidator/Reco'),
    xName = cms.string('pt'),
    xTitle = cms.string('p_{T} [GeV]'),
    xMax = cms.double(200),
    minX = cms.double(0),
    minAbsEta = cms.double(0),
    maxAbsEta = cms.double(3),
    matchThreshold = cms.double(0.5),
    mergeThreshold = cms.double(0.3),
    recoCollection = cms.InputTag('ticlTrackstersCLUE3DHigh'),
    layerClusters = cms.InputTag('hgcalMergeLayerClusters'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
