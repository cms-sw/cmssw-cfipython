import FWCore.ParameterSet.Config as cms

def SiPixelRawToDigi(**kwargs):
  mod = cms.EDProducer('SiPixelRawToDigi',
    IncludeErrors = cms.bool(True),
    UseQualityInfo = cms.bool(False),
    ErrorList = cms.vint32(29),
    UserErrorList = cms.vint32(40),
    InputLabel = cms.InputTag('siPixelRawData'),
    Regions = cms.PSet(
      inputs = cms.optional.VInputTag,
      deltaPhi = cms.optional.vdouble,
      maxZ = cms.optional.vdouble,
      beamSpot = cms.optional.InputTag
    ),
    UsePilotBlade = cms.bool(False),
    UsePhase1 = cms.bool(False),
    CablingMapLabel = cms.string(''),
    SiPixelQualityLabel = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
