import FWCore.ParameterSet.Config as cms

hlt14HLTMhtHtFilterIN4reco7CaloJetEE = cms.EDFilter('HLTCaloMhtHtFilter',
  saveTags = cms.bool(False),
  inputJetTag = cms.InputTag('hltMCJetCorJetIcone5HF07'),
  minMht = cms.double(0),
  minPtJet = cms.vdouble(
    20,
    20
  ),
  minNJet = cms.int32(0),
  mode = cms.int32(2),
  etaJet = cms.vdouble(
    9999,
    9999
  ),
  usePt = cms.bool(True),
  minPT12 = cms.double(0),
  minMeff = cms.double(180),
  meffSlope = cms.double(1),
  minHt = cms.double(0),
  minAlphaT = cms.double(0),
  useTracks = cms.bool(False),
  inputTracksTag = cms.InputTag('hltL3Mouns'),
  triggerType = cms.int32(85)
)
