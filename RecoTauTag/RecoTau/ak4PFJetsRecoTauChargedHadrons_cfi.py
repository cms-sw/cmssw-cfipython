import FWCore.ParameterSet.Config as cms

ak4PFJetsRecoTauChargedHadrons = cms.EDProducer('PFRecoTauChargedHadronProducer',
  verbosity = cms.int32(0),
  maxJetAbsEta = cms.double(2.5),
  outputSelection = cms.string('pt > 0.5'),
  minJetPt = cms.double(14),
  jetSrc = cms.InputTag('ak4PFJets')
)
