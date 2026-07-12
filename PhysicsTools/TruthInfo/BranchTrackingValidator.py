import FWCore.ParameterSet.Config as cms

def BranchTrackingValidator(*args, **kwargs):
  mod = cms.EDProducer('BranchTrackingValidator',
    src = cms.InputTag('truthLogicalGraphProducer'),
    rawSrc = cms.InputTag('truthGraphProducer'),
    hitIndex = cms.InputTag('truthLogicalGraphHitIndexProducer'),
    tracks = cms.InputTag('generalTracks'),
    clusterTPMap = cms.InputTag('tpClusterProducer'),
    folder = cms.string('Tracking/BranchValidator'),
    minPt = cms.double(0.9),
    maxEta = cms.double(3),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
