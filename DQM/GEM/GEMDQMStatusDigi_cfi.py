import FWCore.ParameterSet.Config as cms

GEMDQMStatusDigi = cms.EDProducer('GEMDQMStatusDigi',
  VFATInputLabel = cms.InputTag('muonGEMDigis', 'vfatStatus'),
  GEBInputLabel = cms.InputTag('muonGEMDigis', 'gebStatus'),
  AMCInputLabel = cms.InputTag('muonGEMDigis', 'AMCdata'),
  digisInputLabel = cms.InputTag('muonGEMDigis'),
  AMCSlots = cms.vint32(
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7
  ),
  summaryLabelFmt = cms.string('GE%(station_signed)+i/%(layer)i'),
  flipSummary = cms.bool(False),
  perSuperchamber = cms.bool(True),
  pathOfPrevDQMRoot = cms.string(''),
  numOfEvtPerSec = cms.int32(100),
  secOfEvtPerBin = cms.int32(10),
  totalTimeInterval = cms.int32(50000),
  idxFirstStrip = cms.int32(0),
  bxRange = cms.int32(10),
  bxBin = cms.int32(20),
  mightGet = cms.optional.untracked.vstring
)
