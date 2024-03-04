import FWCore.ParameterSet.Config as cms

def L1TEnergySumFilter(**kwargs):
  mod = cms.EDFilter('L1TEnergySumFilter',
    saveTags = cms.bool(True),
    inputTag = cms.InputTag('L1PFEnergySums'),
    Scalings = cms.PSet(
      theScalings = cms.vdouble(
        0,
        1,
        0
      )
    ),
    TypeOfSum = cms.string('HT'),
    MinPt = cms.double(-1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
