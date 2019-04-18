import FWCore.ParameterSet.Config as cms

hltMhtProducer = cms.EDProducer('HLTMhtProducer',
  usePt = cms.bool(True),
  excludePFMuons = cms.bool(False),
  minNJet = cms.int32(0),
  minPtJet = cms.double(0),
  maxEtaJet = cms.double(999),
  jetsLabel = cms.InputTag('hltAntiKT4PFJets'),
  pfCandidatesLabel = cms.InputTag('hltParticleFlow')
)
