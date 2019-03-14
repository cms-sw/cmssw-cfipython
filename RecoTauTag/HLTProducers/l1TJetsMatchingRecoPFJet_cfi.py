import FWCore.ParameterSet.Config as cms

l1TJetsMatchingRecoPFJet = cms.EDProducer('L1TPFJetsMatching',
  L1JetTrigger = cms.InputTag('hltL1DiJetVBF'),
  JetSrc = cms.InputTag('hltAK4PFJetsTightIDCorrected'),
  pt1Min = cms.double(95),
  pt2Min = cms.double(35),
  mjjMin = cms.double(650),
  matchingR = cms.double(0.5)
)
