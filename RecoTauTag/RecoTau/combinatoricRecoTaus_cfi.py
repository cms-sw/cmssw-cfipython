import FWCore.ParameterSet.Config as cms

combinatoricRecoTaus = cms.EDProducer('RecoTauProducer',
  piZeroSrc = cms.InputTag('ak4PFJetsRecoTauPiZeros'),
  modifiers = cms.required.VPSet,
  jetRegionSrc = cms.InputTag('recoTauAK4PFJets08Region'),
  maxJetAbsEta = cms.double(2.5),
  outputSelection = cms.string('leadPFChargedHadrCand().isNonnull()'),
  chargedHadronSrc = cms.InputTag('ak4PFJetsRecoTauChargedHadrons'),
  minJetPt = cms.double(14),
  jetSrc = cms.InputTag('ak4PFJets'),
  builders = cms.VPSet(
    cms.PSet(
      minAbsPhotonSumPt_insideSignalCone = cms.double(2.5),
      minRelPhotonSumPt_insideSignalCone = cms.double(0.1),
      name = cms.string(''),
      pfCandSrc = cms.InputTag('particleFlow'),
      plugin = cms.string(''),
      verbosity = cms.int32(0)
    )
  ),
  buildNullTaus = cms.bool(False),
  verbosity = cms.int32(0),
  mightGet = cms.optional.untracked.vstring
)
