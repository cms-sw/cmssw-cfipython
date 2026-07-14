import FWCore.ParameterSet.Config as cms

def BranchTrackRecoValidator(*args, **kwargs):
  mod = cms.EDProducer('BranchTrackRecoValidator',
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
    recoCollection = cms.InputTag('generalTracks'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
