import FWCore.ParameterSet.Config as cms

hltPixelVertexCollectionTrimmer = cms.EDProducer('PixelVertexCollectionTrimmer',
  src = cms.InputTag(''),
  maxVtx = cms.uint32(100),
  fractionSumPt2 = cms.double(0.3),
  minSumPt2 = cms.double(0),
  PVcomparer = cms.PSet(
    track_pt_min = cms.double(1),
    track_pt_max = cms.double(10),
    track_chi2_max = cms.double(99999),
    track_prob_min = cms.double(-1)
  )
)
