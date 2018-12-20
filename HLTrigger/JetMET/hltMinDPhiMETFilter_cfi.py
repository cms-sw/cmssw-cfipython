import FWCore.ParameterSet.Config as cms

hltMinDPhiMETFilter = cms.EDFilter('HLTMinDPhiMETFilter',
  saveTags = cms.bool(True),
  usePt = cms.bool(True),
  triggerType = cms.int32(85),
  maxNJets = cms.int32(2),
  minPt = cms.double(30),
  maxEta = cms.double(2.5),
  minDPhi = cms.double(0.5),
  metLabel = cms.InputTag('hltPFMETProducer'),
  calometLabel = cms.InputTag(''),
  jetsLabel = cms.InputTag('hltAK4PFJetL1FastL2L3Corrected')
)
