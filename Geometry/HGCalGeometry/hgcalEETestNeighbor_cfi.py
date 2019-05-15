import FWCore.ParameterSet.Config as cms

hgcalEETestNeighbor = cms.EDAnalyzer('HGCalTestNeighbor',
  detector = cms.string('HGCalEESensitive'),
  pX = cms.vdouble(
    2,
    5,
    10,
    100
  ),
  pY = cms.vdouble(
    2,
    5,
    10,
    100
  ),
  pZ = cms.vdouble(
    10,
    5,
    20,
    50
  )
)
