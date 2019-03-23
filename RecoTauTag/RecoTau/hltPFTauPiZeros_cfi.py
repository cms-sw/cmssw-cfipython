import FWCore.ParameterSet.Config as cms

hltPFTauPiZeros = cms.EDProducer('RecoTauPiZeroProducer',
  massHypothesis = cms.double(0.136),
  verbosity = cms.int32(0),
  maxJetAbsEta = cms.double(99),
  outputSelection = cms.string('pt > 0'),
  minJetPt = cms.double(-1)
)
