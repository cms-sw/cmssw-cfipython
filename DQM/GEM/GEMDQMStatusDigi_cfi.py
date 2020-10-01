import FWCore.ParameterSet.Config as cms

GEMDQMStatusDigi = cms.EDProducer('GEMDQMStatusDigi',
  VFATInputLabel = cms.InputTag('muonGEMDigis', 'vfatStatus'),
  GEBInputLabel = cms.InputTag('muonGEMDigis', 'gebStatus'),
  AMCInputLabel = cms.InputTag('muonGEMDigis', 'AMCdata'),
  digisInputLabel = cms.InputTag('muonGEMDigis'),
  AMCSlots = cms.vint32(
    1,
    3,
    5,
    7,
    9,
    11,
    13,
    15
  ),
  summaryLabelFmt = cms.string('GE%(station_signed)+i/%(layer)i'),
  flipSummary = cms.bool(False),
  perSuperchamber = cms.bool(True),
  idxFirstStrip = cms.int32(0),
  bxRange = cms.int32(10),
  bxBin = cms.int32(20),
  debugMode = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
