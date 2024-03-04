import FWCore.ParameterSet.Config as cms

def HcalRawToDigi(**kwargs):
  mod = cms.EDProducer('HcalRawToDigi',
    HcalFirstFED = cms.untracked.int32(700),
    firstSample = cms.int32(0),
    lastSample = cms.int32(9),
    FilterDataQuality = cms.bool(True),
    FEDs = cms.untracked.vint32(),
    UnpackZDC = cms.untracked.bool(True),
    UnpackCalib = cms.untracked.bool(True),
    UnpackUMNio = cms.untracked.bool(True),
    UnpackTTP = cms.untracked.bool(True),
    silent = cms.untracked.bool(True),
    saveQIE10DataNSamples = cms.untracked.vint32(),
    saveQIE10DataTags = cms.untracked.vstring(),
    saveQIE11DataNSamples = cms.untracked.vint32(),
    saveQIE11DataTags = cms.untracked.vstring(),
    ComplainEmptyData = cms.untracked.bool(False),
    UnpackerMode = cms.untracked.int32(0),
    ExpectedOrbitMessageTime = cms.untracked.int32(-1),
    InputLabel = cms.InputTag('rawDataCollector'),
    ElectronicsMap = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
