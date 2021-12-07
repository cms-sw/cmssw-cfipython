import FWCore.ParameterSet.Config as cms

L1TTkMuonFilter = cms.EDFilter('L1TTkMuonFilter',
  saveTags = cms.bool(True),
  MinPt = cms.double(-1),
  MinEta = cms.double(-5),
  MaxEta = cms.double(5),
  MinN = cms.int32(1),
  inputTag = cms.InputTag('L1TkMuons'),
  applyQuality = cms.bool(True),
  applyDuplicateRemoval = cms.bool(True),
  qualities = cms.PSet(
    values = cms.VPSet(
      cms.PSet(
        detectors = cms.vint32(3),
        qualities = cms.vint32(
          11,
          13,
          14,
          15
        )
      )
    )
  ),
  Scalings = cms.PSet(
    barrel = cms.vdouble(
      0,
      1,
      0
    ),
    overlap = cms.vdouble(
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
