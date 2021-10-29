import FWCore.ParameterSet.Config as cms

l2TauNNProducer = cms.EDProducer('L2TauNNProducer',
  debugLevel = cms.int32(0),
  L1Taus = cms.required.VPSet,
  hbheInput = cms.InputTag(''),
  hoInput = cms.InputTag(''),
  ebInput = cms.InputTag(''),
  eeInput = cms.InputTag(''),
  pataVertices = cms.InputTag('hltPixelVerticesSoA'),
  pataTracks = cms.InputTag('hltPixelTracksSoA'),
  BeamSpot = cms.InputTag(''),
  maxVtx = cms.uint32(100),
  fractionSumPt2 = cms.double(0.3),
  minSumPt2 = cms.double(0),
  track_pt_min = cms.double(1),
  track_pt_max = cms.double(10),
  track_chi2_max = cms.double(99999),
  graphPath = cms.string('RecoTauTag/TrainingFiles/data/L2TauNNTag/L2TauTag_Run3v1.pb'),
  normalizationDict = cms.string('RecoTauTag/TrainingFiles/data/L2TauNNTag/NormalizationDict.json'),
  mightGet = cms.optional.untracked.vstring
)
