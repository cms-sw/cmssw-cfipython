import FWCore.ParameterSet.Config as cms

hosimplereco = cms.EDProducer('HcalSimpleReconstructor',
  correctionPhaseNS = cms.double(13),
  digiLabel = cms.InputTag('hcalDigis'),
  tsFromDB = cms.bool(True),
  samplesToAdd = cms.int32(4),
  Subdetector = cms.string('HO'),
  correctForTimeslew = cms.bool(True),
  dropZSmarkedPassed = cms.bool(True),
  correctForPhaseContainment = cms.bool(True),
  firstSample = cms.int32(4),
  mightGet = cms.optional.untracked.vstring
)
