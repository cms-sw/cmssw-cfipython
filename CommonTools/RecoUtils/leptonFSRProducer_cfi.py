import FWCore.ParameterSet.Config as cms

leptonFSRProducer = cms.EDProducer('LeptonFSRProducer',
  packedPFCandidates = cms.InputTag('packedPFCandidates'),
  slimmedElectrons = cms.InputTag('slimmedElectrons'),
  muons = cms.InputTag('slimmedMuons'),
  electrons = cms.InputTag('slimmedElectrons'),
  muonPtMin = cms.double(3),
  muonEtaMax = cms.double(2.4),
  elePtMin = cms.double(5),
  eleEtaMax = cms.double(2.5),
  photonPtMin = cms.double(2),
  deltaROverEt2Max = cms.double(0.05),
  isolation = cms.double(2),
  mightGet = cms.optional.untracked.vstring
)
