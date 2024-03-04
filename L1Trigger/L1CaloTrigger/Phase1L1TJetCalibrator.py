import FWCore.ParameterSet.Config as cms

def Phase1L1TJetCalibrator(**kwargs):
  mod = cms.EDProducer('Phase1L1TJetCalibrator',
    inputCollectionTag = cms.InputTag('l1tPhase1JetProducer', 'UncalibratedPhase1L1TJetFromPfCandidates'),
    absEtaBinning = cms.required.vdouble,
    calibration = cms.VPSet(
    ),
    outputCollectionName = cms.string('Phase1L1TJetFromPfCandidates'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
