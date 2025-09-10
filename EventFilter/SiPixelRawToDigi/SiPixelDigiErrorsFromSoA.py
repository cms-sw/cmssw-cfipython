import FWCore.ParameterSet.Config as cms

def SiPixelDigiErrorsFromSoA(*args, **kwargs):
  mod = cms.EDProducer('SiPixelDigiErrorsFromSoA',
    digiErrorSoASrc = cms.InputTag('siPixelDigiErrorsSoA'),
    CablingMapLabel = cms.string(''),
    UsePhase1 = cms.bool(False),
    ErrorList = cms.vint32(29),
    UserErrorList = cms.vint32(40),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
