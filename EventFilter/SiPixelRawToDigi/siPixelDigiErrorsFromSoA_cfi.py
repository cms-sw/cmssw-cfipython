import FWCore.ParameterSet.Config as cms

siPixelDigiErrorsFromSoA = cms.EDProducer('SiPixelDigiErrorsFromSoA',
  digiErrorSoASrc = cms.InputTag('siPixelDigiErrorsSoA'),
  CablingMapLabel = cms.string(''),
  UsePhase1 = cms.bool(False),
  ErrorList = cms.vint32(29),
  UserErrorList = cms.vint32(40),
  mightGet = cms.optional.untracked.vstring
)
