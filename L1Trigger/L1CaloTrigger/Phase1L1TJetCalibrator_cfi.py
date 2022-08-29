import FWCore.ParameterSet.Config as cms

Phase1L1TJetCalibrator = cms.EDProducer('Phase1L1TJetCalibrator',
  inputCollectionTag = cms.InputTag('Phase1L1TJetProducer', 'UncalibratedPhase1L1TJetFromPfCandidates'),
  absEtaBinning = cms.required.vdouble,
  calibration = cms.VPSet(
  ),
  outputCollectionName = cms.string('Phase1L1TJetFromPfCandidates'),
  mightGet = cms.optional.untracked.vstring
)
