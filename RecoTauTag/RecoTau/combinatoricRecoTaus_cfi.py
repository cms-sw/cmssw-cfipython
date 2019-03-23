import FWCore.ParameterSet.Config as cms

combinatoricRecoTaus = cms.EDProducer('RecoTauProducer',
  piZeroSrc = cms.InputTag('ak4PFJetsRecoTauPiZeros'),
  jetRegionSrc = cms.InputTag('recoTauAK4PFJets08Region'),
  maxJetAbsEta = cms.double(2.5),
  outputSelection = cms.string('leadPFChargedHadrCand().isNonnull()'),
  chargedHadronSrc = cms.InputTag('ak4PFJetsRecoTauChargedHadrons'),
  minJetPt = cms.double(14),
  jetSrc = cms.InputTag('ak4PFJets'),
  buildNullTaus = cms.bool(False),
  verbosity = cms.int32(0)
)
