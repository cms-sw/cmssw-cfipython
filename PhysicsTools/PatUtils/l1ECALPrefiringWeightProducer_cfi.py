import FWCore.ParameterSet.Config as cms

l1ECALPrefiringWeightProducer = cms.EDProducer('L1ECALPrefiringWeightProducer',
  ThePhotons = cms.InputTag('slimmedPhotons'),
  TheJets = cms.InputTag('slimmedJets'),
  L1Maps = cms.string('L1PrefiringMaps.root'),
  DataEra = cms.string('2017BtoF'),
  UseJetEMPt = cms.bool(False),
  PrefiringRateSystematicUncty = cms.double(0.2),
  JetMaxMuonFraction = cms.double(0.5),
  SkipWarnings = cms.bool(True),
  mightGet = cms.optional.untracked.vstring
)
