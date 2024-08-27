import FWCore.ParameterSet.Config as cms

def SiPixelDigiErrorsFromSoAAlpaka(**kwargs):
  mod = cms.EDProducer('SiPixelDigiErrorsFromSoAAlpaka',
    digiErrorSoASrc = cms.InputTag('siPixelDigis'),
    fmtErrorsSoASrc = cms.InputTag('siPixelDigis'),
    CablingMapLabel = cms.string(''),
    UsePhase1 = cms.bool(False),
    ErrorList = cms.vint32(29),
    UserErrorList = cms.vint32(40),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
