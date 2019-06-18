import FWCore.ParameterSet.Config as cms

pfRecoTauChargedHadronProducer = cms.EDProducer('PFRecoTauChargedHadronProducer',
  ranking = cms.VPSet(
    cms.PSet(
      name = cms.string('ChargedPFCandidate'),
      plugin = cms.string('PFRecoTauChargedHadronStringQuality'),
      selection = cms.string('algoIs("kChargedPFCandidate")'),
      selectionFailValue = cms.double(1000),
      selectionPassFunction = cms.string('-pt')
    )
  ),
  verbosity = cms.int32(0),
  maxJetAbsEta = cms.double(2.5),
  outputSelection = cms.string('pt > 0.5'),
  minJetPt = cms.double(14),
  jetSrc = cms.InputTag('ak4PFJets'),
  builders = cms.VPSet(
    cms.PSet(
      name = cms.string(''),
      plugin = cms.string(''),
      verbosity = cms.int32(0),
      qualityCuts = cms.PSet()
    )
  ),
  mightGet = cms.optional.untracked.vstring
)
