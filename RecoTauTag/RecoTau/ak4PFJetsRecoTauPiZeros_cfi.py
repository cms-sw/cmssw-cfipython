import FWCore.ParameterSet.Config as cms

ak4PFJetsRecoTauPiZeros = cms.EDProducer('RecoTauPiZeroProducer',
  massHypothesis = cms.double(0.136),
  verbosity = cms.int32(0),
  maxJetAbsEta = cms.double(2.5),
  outputSelection = cms.string('pt > 1.5'),
  minJetPt = cms.double(14),
  jetSrc = cms.InputTag('ak4PFJets')
)
