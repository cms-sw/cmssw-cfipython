import FWCore.ParameterSet.Config as cms

Phase1L1TJetSumsProducer = cms.EDProducer('Phase1L1TJetSumsProducer',
  inputJetCollectionTag = cms.InputTag('l1tPhase1JetCalibrator', 'Phase1L1TJetFromPfCandidates'),
  sinPhi = cms.required.vdouble,
  cosPhi = cms.required.vdouble,
  nBinsPhi = cms.uint32(72),
  phiLow = cms.double(-3.1415926535897931),
  phiUp = cms.double(3.1415926535897931),
  htPtThreshold = cms.double(30),
  mhtPtThreshold = cms.double(30),
  htAbsEtaCut = cms.double(3),
  mhtAbsEtaCut = cms.double(3),
  ptlsb = cms.double(0.25),
  outputCollectionName = cms.string('Sums'),
  mightGet = cms.optional.untracked.vstring
)
