import FWCore.ParameterSet.Config as cms

hltMhtProducer = cms.EDProducer('HLTMhtProducer',
  inputJetTag = cms.InputTag('hltMCJetCorJetIcone5HF07'),
  minPtJet = cms.double(20),
  etaJet = cms.double(9999),
  usePt = cms.bool(True)
)
