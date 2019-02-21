import FWCore.ParameterSet.Config as cms

pfJetMETcorrInputProducerTRecoPFJetJetCorrExtractorTRecoPFJet = cms.EDProducer('PFJetMETcorrInputProducer',
  src = cms.InputTag('ak4PFJetsCHS'),
  offsetCorrLabel = cms.InputTag('ak4PFCHSL1FastjetCorrector'),
  jetCorrLabel = cms.InputTag('ak4PFCHSL1FastL2L3Corrector'),
  jetCorrLabelRes = cms.InputTag('ak4PFCHSL1FastL2L3ResidualCorrector'),
  jetCorrEtaMax = cms.double(9.9),
  type1JetPtThreshold = cms.double(15),
  skipEM = cms.bool(True),
  skipEMfractionThreshold = cms.double(0.9),
  skipMuons = cms.bool(True),
  skipMuonSelection = cms.string('isGlobalMuon | isStandAloneMuon')
)
