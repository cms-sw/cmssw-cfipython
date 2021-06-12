import FWCore.ParameterSet.Config as cms

l1PrefiringWeightProducer = cms.EDProducer('L1PrefiringWeightProducer',
  TheMuons = cms.InputTag('slimmedMuons'),
  ThePhotons = cms.InputTag('slimmedPhotons'),
  TheJets = cms.InputTag('slimmedJets'),
  L1Maps = cms.string('L1PrefiringMaps.root'),
  L1MuonParametrizations = cms.string('L1MuonPrefiringParametriations.root'),
  DataEraECAL = cms.string('2017BtoF'),
  DataEraMuon = cms.string('2016'),
  UseJetEMPt = cms.bool(False),
  DoMuons = cms.bool(True),
  PrefiringRateSystematicUnctyECAL = cms.double(0.2),
  PrefiringRateSystematicUnctyMuon = cms.double(0.2),
  JetMaxMuonFraction = cms.double(0.5)
)
