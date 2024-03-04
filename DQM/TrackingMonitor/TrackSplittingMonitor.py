import FWCore.ParameterSet.Config as cms

def TrackSplittingMonitor(**kwargs):
  mod = cms.EDProducer('TrackSplittingMonitor',
    FolderName = cms.string('TrackSplitMonitoring'),
    splitTrackCollection = cms.InputTag('splittedTracksP5'),
    splitMuonCollection = cms.InputTag('splitMuons'),
    ifPlotMuons = cms.bool(True),
    pixelHitsPerLeg = cms.int32(1),
    totalHitsPerLeg = cms.int32(6),
    d0Cut = cms.double(12),
    dzCut = cms.double(25),
    ptCut = cms.double(4),
    norchiCut = cms.double(100),
    ddxyBin = cms.int32(100),
    ddxyMin = cms.double(-200),
    ddxyMax = cms.double(200),
    ddzBin = cms.int32(100),
    ddzMin = cms.double(-400),
    ddzMax = cms.double(400),
    dphiBin = cms.int32(100),
    dphiMin = cms.double(-0.01),
    dphiMax = cms.double(0.01),
    dthetaBin = cms.int32(100),
    dthetaMin = cms.double(-0.01),
    dthetaMax = cms.double(0.01),
    dptBin = cms.int32(100),
    dptMin = cms.double(-5),
    dptMax = cms.double(5),
    dcurvBin = cms.int32(100),
    dcurvMin = cms.double(-0.005),
    dcurvMax = cms.double(0.005),
    normBin = cms.int32(100),
    normMin = cms.double(-5),
    normMax = cms.double(5),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
