import FWCore.ParameterSet.Config as cms

hltAlphaTFilterRecoPFJet = cms.EDFilter('HLTAlphaTPFJetFilter',
  saveTags = cms.bool(True),
  inputJetTag = cms.InputTag('hltMCJetCorJetIcone5HF07'),
  inputJetTagFastJet = cms.InputTag('hltMCJetCorJetIcone5HF07'),
  minPtJet = cms.vdouble(
    20,
    20
  ),
  minNJet = cms.int32(0),
  etaJet = cms.vdouble(
    9999,
    9999
  ),
  maxNJets = cms.uint32(32),
  minHt = cms.double(0),
  minAlphaT = cms.double(0),
  triggerType = cms.int32(85),
  dynamicAlphaT = cms.bool(True),
  setDHtZero = cms.bool(False)
)
