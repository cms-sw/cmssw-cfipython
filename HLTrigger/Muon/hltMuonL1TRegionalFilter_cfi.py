import FWCore.ParameterSet.Config as cms

hltMuonL1TRegionalFilter = cms.EDFilter('HLTMuonL1TRegionalFilter',
  saveTags = cms.bool(True),
  CandTag = cms.InputTag('hltGmtStage2Digis'),
  PreviousCandTag = cms.InputTag('hltL1sL1SingleMu20'),
  MinN = cms.int32(1),
  CentralBxOnly = cms.bool(True),
  Cuts = cms.VPSet(
    cms.PSet(
      EtaRange = cms.vdouble(
        -2.5,
        -1.6
      ),
      MinPt = cms.double(20),
      QualityBits = cms.vuint32(
        6,
        7
      )
    ),
    cms.PSet(
      EtaRange = cms.vdouble(
        -1.6,
        1.6
      ),
      MinPt = cms.double(20),
      QualityBits = cms.vuint32(7)
    ),
    cms.PSet(
      EtaRange = cms.vdouble(
        1.6,
        2.5
      ),
      MinPt = cms.double(20),
      QualityBits = cms.vuint32(
        6,
        7
      )
    )
  )
)
