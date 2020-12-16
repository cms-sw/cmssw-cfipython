import FWCore.ParameterSet.Config as cms

L1TTkEmFilter = cms.EDFilter('L1TTkEmFilter',
  saveTags = cms.bool(True),
  MinPt = cms.double(-1),
  MinEta = cms.double(-5),
  MaxEta = cms.double(5),
  MinN = cms.int32(1),
  inputTag1 = cms.InputTag('L1TkEms1'),
  inputTag2 = cms.InputTag('L1TkEms2'),
  EtaBinsForIsolation = cms.vdouble(
    0,
    1.479
  ),
  TrkIsolation = cms.vdouble(99999.9),
  Quality1 = cms.int32(0),
  Quality2 = cms.int32(0),
  Qual1IsMask = cms.bool(False),
  Qual2IsMask = cms.bool(False),
  ApplyQual1 = cms.bool(False),
  ApplyQual2 = cms.bool(False),
  Scalings = cms.PSet(
    barrel = cms.vdouble(
      0,
      1,
      0
    ),
    endcap = cms.vdouble(
      0,
      1,
      0
    )
  ),
  mightGet = cms.optional.untracked.vstring
)
