import FWCore.ParameterSet.Config as cms

hltDisplacedEgammaFilter = cms.EDFilter('HLTDisplacedEgammaFilter',
  saveTags = cms.bool(True),
  inputTag = cms.InputTag('hltEGRegionalL1SingleEG22'),
  l1EGCand = cms.InputTag('hltL1IsoRecoEcalCandidate'),
  RecHitsEB = cms.InputTag('hltEcalRecHit', 'EcalRecHitsEB'),
  RecHitsEE = cms.InputTag('hltEcalRecHit', 'EcalRecHitsEE'),
  inputTrack = cms.InputTag('hltL1SeededEgammaRegionalCTFFinalFitWithMaterial'),
  ncandcut = cms.int32(1),
  EBOnly = cms.bool(False),
  sMin_min = cms.double(0.1),
  sMin_max = cms.double(0.4),
  sMaj_min = cms.double(0),
  sMaj_max = cms.double(999),
  seedTimeMin = cms.double(-25),
  seedTimeMax = cms.double(25),
  maxTrackCut = cms.int32(0),
  trackPtCut = cms.double(3),
  trackdRCut = cms.double(0.5)
)
