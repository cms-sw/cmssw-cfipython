import FWCore.ParameterSet.Config as cms

hfsimplereco = cms.EDProducer('HcalSimpleReconstructor',
  correctionPhaseNS = cms.double(0),
  digiLabel = cms.InputTag('hcalDigis'),
  tsFromDB = cms.bool(True),
  samplesToAdd = cms.int32(2),
  Subdetector = cms.string('HF'),
  correctForTimeslew = cms.bool(False),
  dropZSmarkedPassed = cms.bool(True),
  correctForPhaseContainment = cms.bool(False),
  firstSample = cms.int32(4),
  mightGet = cms.optional.untracked.vstring
)
