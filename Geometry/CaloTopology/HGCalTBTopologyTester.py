import FWCore.ParameterSet.Config as cms

def HGCalTBTopologyTester(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalTBTopologyTester',
    detectorName = cms.string('HGCalEESensitive'),
    types = cms.vint32(
      0,
      0,
      0,
      0,
      0,
      0,
      1,
      1,
      1,
      1,
      1,
      1,
      2,
      2,
      2,
      2,
      2,
      2
    ),
    layers = cms.vint32(
      1,
      2,
      3,
      4,
      5,
      6,
      7,
      8,
      9,
      10,
      11,
      12,
      13,
      14,
      15,
      16,
      17,
      18
    ),
    sector = cms.vint32(
      1,
      1,
      2,
      2,
      3,
      3,
      5,
      5,
      6,
      6,
      7,
      7,
      8,
      8,
      9,
      9,
      10,
      10
    ),
    cells = cms.vint32(
      0,
      4,
      12,
      14,
      18,
      23,
      1,
      4,
      7,
      10,
      13,
      16,
      0,
      3,
      6,
      9,
      12,
      15
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
