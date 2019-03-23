import FWCore.ParameterSet.Config as cms

pfJetsLegacyHPSPiZeros = cms.EDProducer('RecoTauPiZeroProducer',
  massHypothesis = cms.double(0.136),
  verbosity = cms.int32(0),
  maxJetAbsEta = cms.double(2.5),
  outputSelection = cms.string('pt > 0'),
  minJetPt = cms.double(14),
  jetSrc = cms.InputTag('ak4PFJets')
)
