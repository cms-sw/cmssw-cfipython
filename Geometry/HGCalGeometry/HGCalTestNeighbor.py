import FWCore.ParameterSet.Config as cms

def HGCalTestNeighbor(**kwargs):
  mod = cms.EDAnalyzer('HGCalTestNeighbor',
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
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
